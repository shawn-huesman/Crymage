from PIL import Image
import os
from functools import lru_cache


class Cipher:

    def __init__(self, *, in_url: str):
        self.in_url = in_url
        self.img = Image.open(in_url, 'r')

        # array with a 3-tuple storing (R,G,B) values as each element
        self.pixel_array = self.img.load()

        # copied to use for positional encoding and decoding
        self.pixel_array_copy = self.img.copy().load()

        # image resolution represented as xres x yres Examples: 1920x1080 (xres=1920, yres=1080)
        self.xres, self.yres = self.img.size

    def encode_caesar(self, key: int):
        self._transcode("caesar", decode=False, credentials=[key])

    def decode_caesar(self, key: int):
        self._transcode("caesar", decode=True, credentials=[key])

    def encode_multiplicative(self, xkey: int, ykey: int):
        self._transcode("multiplicative", decode=False, credentials=[xkey, ykey])

    def decode_multiplicative(self, xkey: int, ykey: int):
        self._transcode("multiplicative", decode=True, credentials=[xkey, ykey])

    def encode_affine(self, xkey: int, ykey: int, shift_key: int):
        self._transcode("affine", decode=False, credentials=[xkey, ykey, shift_key])

    def decode_affine(self, xkey: int, ykey: int, shift_key: int):
        self._transcode("affine", decode=True, credentials=[xkey, ykey, shift_key])

    def encode_vigenere(self, keyword: str):
        self._transcode("vigenere", decode=False, credentials=[keyword])

    def decode_vigenere(self, keyword: str):
        self._transcode("vigenere", decode=True, credentials=[keyword])

    def _transcode(self, cipher_name: str, *, decode: bool, credentials: list):
        available_ciphers = ["caesar", "multiplicative", "affine", "vigenere"]

        if cipher_name not in available_ciphers:
            raise ValueError("Not a valid cipher name. Valid cipher names include: " + str(available_ciphers))

        if cipher_name == "multiplicative" or cipher_name == "affine":
            mult_inverse_table_x = self.calculate_multiplicative_keys(self.xres)
            mult_inverse_table_y = self.calculate_multiplicative_keys(self.yres)

        for i in range(0, self.xres):
            for j in range(0, self.yres):
                shift_index_i = i
                shift_index_j = j

                if cipher_name == "caesar":
                    key = credentials[0]

                    if decode:
                        shift_index_i = (i + abs(self.xres - key)) % self.xres
                        shift_index_j = (j + abs(self.yres - key)) % self.yres

                    else:  # encoding caesar
                        shift_index_i = (i + key) % self.xres
                        shift_index_j = (j + key) % self.yres

                elif cipher_name == "multiplicative":
                    xkey = credentials[0]
                    ykey = credentials[1]
                    if xkey not in mult_inverse_table_x:
                        raise ValueError("Key not valid for x resolution range 0-" + str(self.xres))
                    if ykey not in mult_inverse_table_y:
                        raise ValueError("Key not valid for y resolution range 0-" + str(self.yres))

                    if decode:
                        shift_index_i = (i * mult_inverse_table_x[xkey]) % self.xres
                        shift_index_j = (j * mult_inverse_table_y[ykey]) % self.yres
                    else:
                        shift_index_i = (i * xkey) % self.xres
                        shift_index_j = (j * ykey) % self.yres

                elif cipher_name == "affine":
                    xkey = credentials[0]
                    ykey = credentials[1]
                    shift_key = credentials[2]
                    if xkey not in mult_inverse_table_x:
                        raise ValueError("Key not valid for x resolution range 0-" + str(self.xres))
                    if ykey not in mult_inverse_table_y:
                        raise ValueError("Key not valid for y resolution range 0-" + str(self.yres))

                    if decode:
                        shift_index_i = (mult_inverse_table_x[xkey] * (i - shift_key)) % self.xres
                        shift_index_j = (mult_inverse_table_y[ykey] * (j - shift_key)) % self.yres
                    else:
                        shift_index_i = ((i * xkey) + shift_key) % self.xres
                        shift_index_j = ((j * ykey) + shift_key) % self.yres

                elif cipher_name == "vigenere":
                    keyword = credentials[0]
                    xkeyword = self.create_extended_keyword(self, keyword, self.xres)
                    ykeyword = self.create_extended_keyword(self, keyword, self.yres)

                    xkey = ord(xkeyword[i]) - 96
                    ykey = ord(ykeyword[j]) - 96

                    if decode:
                        shift_index_i = (i + abs(self.xres - xkey)) % self.xres
                        shift_index_j = (j + abs(self.yres - ykey)) % self.yres

                    else:  # encoding caesar
                        shift_index_i = (i + xkey) % self.xres
                        shift_index_j = (j + ykey) % self.yres

                self.pixel_array[i, j] = self.pixel_array_copy[shift_index_i, shift_index_j]
        self.img.save(self._create_dir(is_decoding=True if decode else False))

    @staticmethod
    def create_extended_keyword(self, keyword, length):
        pre_keyword = "".join(str.lower(keyword).split())
        keyword = "".join([i for i in pre_keyword if i.isalpha()])
        repeated_keyword = keyword * length
        return repeated_keyword[0:length]

    @staticmethod
    def calculate_multiplicative_keys(upper_alphabet_bound: int):
        """
        :param upper_alphabet_bound: alphabet is range (0, upper_alphabet_bound) (i.e xres of image is 1920, therefore
        the alphabet of the image is 0-1919 (1920 pixels). For this example, upper alphabet bound = 1920

        :return: dictionary of usable keys for multiplicative cipher along with their inverses.
        For example, if the return was {(5,3) (3,5)}, then the only usable keys are 5 and 3 and they are inverses of
        each other
        """

        def gcd(p, q):
            # Create the gcd of two positive integers.
            while q != 0:
                p, q = q, p % q
            return p

        def is_coprime(x, y):
            return gcd(x, y) == 1

        def phi_func(x):
            if x == 1:
                return 1
            else:
                n = [y for y in range(1, x) if is_coprime(x, y)]
                return n

        multiplicative_values = phi_func(upper_alphabet_bound - 1)
        cipher_table = dict()
        for i in multiplicative_values:
            for j in multiplicative_values:
                if i not in cipher_table:  # implies j is also not in table
                    if (i * j) % upper_alphabet_bound == 1:
                        cipher_table[i] = j
                        cipher_table[j] = i
        return cipher_table

    def _create_dir(self, *, is_decoding: bool):
        if is_decoding:
            out_folder = "Decoded_Images"
        else:
            out_folder = "Encoded_Images"

        img_dir = os.getcwd() + '\\' + out_folder
        img_filename = os.path.basename(self.in_url)

        os.makedirs(img_dir, exist_ok=True)
        return_dir = img_dir + '\\' + img_filename
        return return_dir
