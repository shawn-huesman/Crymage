from Ciphers import Cipher


def main():
    #  file_path = r"C:\Users\Shawn Huesman\Downloads\Evariste_galois.jpg"
    file_path = r"C:\Users\Shawn Huesman\Github\Crymage\Examples\Encoded_Images\multiencoded.jpg"
    mcipher = Cipher(in_url=file_path)
    Cipher.decode_multiplicative(mcipher, 667, 905)


if __name__ == "__main__":
    main()