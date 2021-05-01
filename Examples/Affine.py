from Ciphers import Cipher


def main():
    # file_path = r"galois.jpg"
    file_path = r"Examples\Encoded_Images\galois.jpg"
    mcipher = Cipher(in_url=file_path)
    Cipher.decode_affine(mcipher, 667, 905, 500)


if __name__ == "__main__":
    main()