from cryptography.fernet import Fernet

def genewrite_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

def get_key():
    key = open("pass.key", "rb").read()
    return  key

genewrite_key()
password = input("Enter password to encrypt :")
text = password.encode()
key = get_key()
fernet = Fernet(key=key)
encrypted_password = fernet.encrypt(text)
print(encrypted_password)

decode_text = fernet.decrypt(encrypted_password)
plain_text_decoded = bytes(decode_text).decode("utf-8")
print(plain_text_decoded)