import binascii
from image import encryptImage, decryptImage
from ECB import convertToListInt

filePath ="C:/Users/HP/Downloads/436611014_7612713615489080_7911857705770275772_n.jpg"
print("Tiny Encryption Algorithm (TEA) Encryption/Decryption")

key_hex=input("Enter key in 16 Hex character:")
#key_hex = "1a2b3c4d5e6f7890123456789abcdef0"
key = binascii.unhexlify(key_hex)
key = convertToListInt(key)
mode = input("Run for ECB mode of TEA or CBC mode of TEA: ").upper()
IV = None
if mode == "CBC":
    IV_hex=input("Enter IV in 16 Hex character:")
    #IV_hex = "12345678abcdef90"
    IV = binascii.unhexlify(IV_hex)

action = input("Encrypt or Decrypt (E/D): ").upper()
if action == "E":
    encryptImage(filePath, key, mode, IV)
    if mode == "ECB":
        print("Operation Done, Image saved as EncryptedImageECB.png")
    else:
        print("Operation Done, Image saved as EncryptedImageCBC.png")

elif action == "D":
    decryptImage(filePath, key, mode, IV)
    if mode == "ECB":
        print("Operation Done, Image saved as DecryptedImageECB.png")
    else:
        print("Operation Done, Image saved as DecryptedImageCBC.png")
