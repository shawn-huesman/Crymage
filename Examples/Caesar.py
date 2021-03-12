from Ciphers import Cipher


def main():
    file_path = r"C:\Users\Shawn Huesman\Downloads\Evariste_galois.jpg"
    # file_path = r"C:\Users\Shawn Huesman\Github\Crymage\Examples\Encoded_Images\multiencoded.jpg"
    mcipher = Cipher(in_url=file_path)
    Cipher.encode_caesar(mcipher, 500)


if __name__ == "__main__":
    main()