from pyfiglet import figlet_format
from stegano import lsb
from cryptography.fernet import Fernet
from PIL import Image
import imagehash
import hashlib
from pathlib import Path

def intro():
    print("\nHello, Thank you so much for using this program :)")
    print("This program works on a very simple interface.")
    print("For example:")
    print("You are provided with a list from following options")
    print("1. Apple")
    print("2. Banana")
    print("Say you want to choose the banana, Enter 2 in the field below")
    _ = input("Input Field >>> ")
    if "2" == _:
        print("And that's how it works")
        print("Now look at your options and start using the program")


def txthash(txt):
        print("\nHashing Algorithms supported:>")
        print("0. md5")
        print("1. sha256")
        print("2. sha1")
        print("3. sha224")
        print("4. sha384")
        print("5. sha512")
        print("6. sha3_224")
        print("7. sha3_256")
        print("8. sha3_384")
        print("9. sha3_512")
        print("10. blake2s")
        print("11. blake2b")
        alg = input("Please select your option >>> ")
        if alg == "0":
            hash = hashlib.md5(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "1":
            hash = hashlib.sha256(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "2":
            hash = hashlib.sha1(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "3":
            hash = hashlib.sha224(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "4":
            hash = hashlib.sha384(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "5":
            hash = hashlib.sha512(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "6":
            hash = hashlib.sha3_224(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "7":
            hash = hashlib.sha3_256(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "8":
            hash = hashlib.sha3_384(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "9":
            hash = hashlib.sha3_512(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "10":
            hash = hashlib.blake2s(txt.encode())
            print("Hash:"+hash.hexdigest())
        elif alg == "11":
            hash = hashlib.blake2b(txt.encode())
            print("Hash:"+hash.hexdigest())

def imghash(x):
    print("Hashing Algorithms supported:>\n")
    print("1. Average Hashing")
    print("2. Perceptual Hashing")
    print("3. Difference Hashing")
    print("4. Wavelet Hashing")
    print("5. Crop Resistant Hashing")
    print("6. Colour Hash")
    alg = input("Choose the hashing algorithm >>> ")
    img = Image.open(x)
    if alg == "1":
        hash = imagehash.average_hash(img)
        print(hash)
    elif alg == "2":
        hash = imagehash.phash(img)
        print(hash)
    elif alg == "3":
        hash = imagehash.dhash(img)
        print(hash)
    elif alg == "4":
        hash = imagehash.whash(img)
        print(hash)
    elif alg == "5":
        hash = imagehash.crop_resistant_hash(img)
        print(hash)    
    elif alg == "6":
        hash = imagehash.colorhash(img)
        print(hash)

def main():
    print(figlet_format("The Crypt"))
    print("****************************************************************")
    print("* Copyright of Rahul Gonal                                     *")
    print("* https://github.com/Rahul-Gonal                               *")
    print("* Only For Educational Purposes :)                             *")
    print("****************************************************************\n")
    print("0. Intro for new users")
    print("1. Text into hash")
    print("2. Hash an Image")
    print("3. Encode text in image")
    print("4. Decode text in image")
    print("5. Hash a text file")
    print("\nCtrl+c for Exit")
    while True:
        opt = input("Please select your option >>> ")

        try:
            if "0" == opt:
                intro()
                

            elif ("1") == opt:
                var = input("Enter text to be hashed >>> ")
                txthash(var)

            elif "2" == opt:
                imgpath = input("Enter path of Image file >>> ")
                imghash(imgpath)

            elif "3" == opt:
                encpath = input("Enter path of Image file to encode >>> ")
                print("Include Filenames in both the inputs")
                decpath = input("Enter path of the image file to be produced as Output >>> ")
                code = input("Enter the text to be encoded >>> ")
                img = lsb.hide(str(encpath),str(code))
                img.save(str(decpath))
                print("Succesfully encoded the text in the image.")

            elif "4" == opt:
                decpath = input("Enter the path of the Image file to be decoded >>> ")
                code = lsb.reveal(str(decpath))
                print("Text succesfully Decoded")
                print(code)

            elif "5" == opt:
                path = input("Enter the path of the file >>> ")
                lines = Path(path).read_text()
                txthash(lines)

        except (KeyboardInterrupt,EOFError):
                break

if __name__ == "__main__":
    main()