# The-Crypt
One-stop for all your cryptography needs in python

<p align="center">
  <img src="https://github.com/Rahul-Gonal/The-Crypt/blob/main/Logo.png" />
</p>


![MadeByRahul](https://img.shields.io/badge/Made%20By-RahulGonal-orange)
![MadeWithPython](https://img.shields.io/badge/Made%20With-Python-blue)
![Passed](https://img.shields.io/badge/Tests-Succesfully%20Passed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

## Introduction
This is The Crypt, a python program designed to be one-stop solution for all the basic cryptographic and steganographic needs of programmers.
It uses various python modules for hashing and encryption all of which can be installed using pip.
It also has a friendly intro for using the interface built in the program itself.

## Features

### 1. Text into Hash
The Crypt supports conversion of a user-given string directly into hash using the hashlib module and supports the following algorithms:
1. md5
2. sha256
3. sha1
4. sha224
5. sha384
6. sha512
7. sha3_224
8. sha3_256
9. sha3_384
10. sha3_512
11. blake2s
12. blake2b

### 2. Image Hashing
The Crypt supports hashing of images using the ImageHash module in python. The program recieves the path of the image file from the user and opens it using PIL.Image. The ImageHash module then comes into play and converts the image into hash which is option based on the following algorithms:
1. Average Hashing
2. Perceptual Hashing
3. Difference Hashing
4. Wavelet Hashing
5. Crop Resistant Hashing
6. Colour Hash

### 3. Encode text in an image (Steganography)
The Crypt using the stegano module can embed messages into image once it recives the path file of the image. The user is also prompted for a path to output the image "which must contain the filename at the end even if it doesn't exist". Refer to the [stegano](https://pypi.org/project/stegano/) docs for more info.

### 4. Decode text from an image
The Crypt supports the decryption of text from the image using the same stegano module with the path of the image file.

### 5. Hash text from a file
The Crypt supports hashing of text from a file using pathlib and hashlib. This has only been tested for txt files.
