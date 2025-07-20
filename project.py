
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def get_aes_key_from_string(s: str, key_size=16) -> bytes:
    assert key_size in (16, 24, 32), "Invalid key size"
    hash_bytes = hashlib.sha256(s.encode()).digest()
    return hash_bytes[:key_size]

def encrypt(plainbytes: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plainbytes, AES.block_size)
    return cipher.encrypt(padded)

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted

def encode_file(full_path: str, entered_key: str):
    with open(full_path, "rb") as input_file:
        file_bytes = input_file.read()

    encoded_bytes = encrypt(file_bytes, get_aes_key_from_string(entered_key))

    encoded_file_path = full_path+".encoded"
    with open(encoded_file_path, "wb") as encoded_file:
        encoded_file.write("<<<EncodedWithTrampoline>>>".encode() + encoded_bytes + "<<<EncodedWithTrampoline>>>".encode())
    
    return encoded_file_path

def decode_file(full_path: str, entered_key: str):
    with open(full_path, "rb") as encoded_file:
        encoded_bytes = encoded_file.read()

    encoded_bytes = encoded_bytes.removeprefix(b"<<<EncodedWithTrampoline>>>")
    encoded_bytes = encoded_bytes.removesuffix(b"<<<EncodedWithTrampoline>>>")

    decoded_bytes = decrypt(encoded_bytes, get_aes_key_from_string(entered_key))

    directory = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)

    file_name = "decoded_" + file_name.removesuffix(".encoded")

    new_path = os.path.join(directory, file_name)

    with open(new_path, "wb") as decoded_file:
        decoded_file.write(decoded_bytes)
    
    return new_path

def get_list_of_encoded_files(directory_path):

    list_of_files = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            if check_validity(full_path):
                list_of_files.append(full_path)

    return list_of_files

def check_validity(full_path):

    with open(full_path, "rb") as encoded_file:
        encoded_bytes = encoded_file.read()

    if encoded_bytes.startswith(b"<<<EncodedWithTrampoline>>>") and encoded_bytes.endswith(b"<<<EncodedWithTrampoline>>>"):
        return True
    
    return False


def main():
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
            full_path = input("Enter the file full path: ")
            entered_key = input("Enter a key to encrypt the file with: ")

            encryption_path = encode_file(full_path, entered_key)

            print("Encryption Done")
            print("Encryption file:", encryption_path)
        
        elif inp == "2":
            directory_path = input("Enter the full path of the directory: ")

            list_of_files = get_list_of_encoded_files(directory_path)

            for f in list_of_files:
                print(f, "is encoded")
            
            if not list_of_files:
                print("No encoded files are found in this directory")
            
        elif inp == "3":
            full_path = input("Enter the full path of the encoded file: ")
            entered_key = input("Enter the key you used to encode: ")

            if check_validity(full_path):

                decryption_path = decode_file(full_path, entered_key)
                
                print("Decryption Done")
                print("Decryption file:", decryption_path)
        
        elif inp == "0":
            print("Exiting the program.")
            exit()
        
        else:
            print("Invalid input")
        
        print("\n")


if __name__ == "__main__":
    main()



