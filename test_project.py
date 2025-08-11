from project import get_aes_key_from_string, encrypt, decrypt, encode_file, decode_file
import os

def test_get_aes_key_from_string():

    assert get_aes_key_from_string("somephrase", 32).hex() == "885d9e9506c1c67cc5ac035c259d922f103a00de4abf41517421f27151f0d5e5"
    assert get_aes_key_from_string("heyhey", 16).hex() == "db9e0e81988b9b0e007d67caa8c67eae"
    assert get_aes_key_from_string("joemontana", 24).hex() == "c2b1894dd9610b3b91203f5193d3cc39ccaf37c491cc5635"


def test_encrypt():

    assert encrypt("amazing".encode(), get_aes_key_from_string("awesome")).hex() == "10df487eb7ccd036ecb4f2aea22706ae"

def test_decrypt():

    assert decrypt(bytes.fromhex("10df487eb7ccd036ecb4f2aea22706ae"), get_aes_key_from_string("awesome")).decode() == "amazing"


def test_process():

    before_content = "Hey, how are you doing here."
    chosen_key = "smartpassword"

    original_file_path = os.path.join(os.getcwd(), "testfile.txt")
    with open(original_file_path, "w") as test_file:
        test_file.write(before_content)

    encoded_file_path = encode_file(original_file_path, chosen_key)

    decoded_file_path = decode_file(encoded_file_path, chosen_key)

    with open(decoded_file_path, "r") as decoded_file:
        after_content = decoded_file.read()

    assert before_content == after_content