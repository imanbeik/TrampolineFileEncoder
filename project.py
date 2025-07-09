
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def get_aes_key_from_string(s: str, key_size=16) -> bytes:
    assert key_size in (16, 24, 32), "Invalid key size"
    hash_bytes = hashlib.sha256(s.encode()).digest()  # 32 bytes
    return hash_bytes[:key_size]

def encrypt(plainbytes: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plainbytes, AES.block_size)
    return cipher.encrypt(padded)

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted


if __name__ == "__main__":
    print("Welcome to file encoder :)")

    while True:
        inp = input("What do you want to do?" \
            "\n\t1: Encode a file" \
            "\n\t2: List of encoded files in a directory" \
            "\n\t3: Decode a file" \
            "\n\t0: Exit" \
            "\n: "
        )

        if inp == "1":
            inp2 = input("Enter the file full path: ")
            inp3 = input("Enter a key to encrypt the file with: ")

            with open(inp2, "rb") as input_file:
                file_bytes = input_file.read()

            encoded_bytes = encrypt(file_bytes, get_aes_key_from_string(inp3))

            with open(inp2+".encoded", "wb") as encoded_file:
                encoded_file.write("<<<EncodedWithTrampoline>>>".encode() + encoded_bytes + "<<<EncodedWithTrampoline>>>".encode())

            print("Encryption Done")
        
        elif inp == "2":
            inp2 = input("Enter the full path of the directory: ")

            there_was = False

            for entry in os.listdir(inp2):
                full_path = os.path.join(inp2, entry)
                if os.path.isfile(full_path):
                    with open(full_path, "rb") as a_file:
                        if a_file.read().startswith(b"<<<EncodedWithTrampoline>>>"):
                            print(full_path, "is encoded")
                            there_was = True
            
            if not there_was:
                print("No encoded files are found in this directory")
            
        elif inp == "3":
            inp2 = input("Enter the full path of the encoded file: ")
            inp3 = input("Enter the key you used to encode: ")

            encoded_file = open(inp2, "rb")

            encoded_bytes = encoded_file.read()

            if encoded_bytes.startswith(b"<<<EncodedWithTrampoline>>>") and encoded_bytes.endswith(b"<<<EncodedWithTrampoline>>>"):
                encoded_bytes = encoded_bytes.removeprefix(b"<<<EncodedWithTrampoline>>>")
                encoded_bytes = encoded_bytes.removesuffix(b"<<<EncodedWithTrampoline>>>")

                decoded_bytes = decrypt(encoded_bytes, get_aes_key_from_string(inp3))

                directory = os.path.dirname(inp2)
                file_name = os.path.basename(inp2)

                file_name = "decoded_" + file_name.removesuffix(".encoded")

                new_path = os.path.join(directory, file_name)

                with open(new_path, "wb") as decoded_file:
                    decoded_file.write(decoded_bytes)
                
                print("Decryption Done")
        
        elif inp == "0":
            print("Exiting the program.")
            exit()
        
        else:
            print("Invalid input")
        
        print("\n")



