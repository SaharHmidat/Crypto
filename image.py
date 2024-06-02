from PIL import Image
from ECB import ECBEncryption, ECBDecryption
from CBC import CBCEncryption, CBCDecryption



def encryptImage(filePath, key, mode, IV=None):
    with Image.open(filePath) as img:
        img_bytes = img.tobytes()
        tenBlocks = img_bytes[:10 * 8]  # assume block size = 8 bytes,get the first 10 blocks
        remainBlocks = img_bytes[10 * 8:]   # encrypt the remaining blocks
        if mode == "ECB":
            encryptedRemainBlocks = ECBEncryption(remainBlocks, key)
        elif mode == "CBC":
            encryptedRemainBlocks = CBCEncryption(remainBlocks, key, IV)
        encrypted_bytes = tenBlocks + encryptedRemainBlocks # get all encryption

        encrypted_image = Image.frombytes(img.mode, img.size, encrypted_bytes)
        grayscale_encrypted_image = encrypted_image.convert("L")
        grayscale_encrypted_image.show()

        if mode == "ECB":
            grayscale_encrypted_image.save("EncryptedImageECB.png")
        else:
            grayscale_encrypted_image.save("EncryptedImageCBC.png")


from PIL import Image


def decryptImage(filePath, key, mode, IV=None):
    with Image.open(filePath) as img:
        img_bytes = img.tobytes()

        tenBlocks = img_bytes[:10 * 8]  # assume block size = 8 bytes, keep the first 10 blocks
        remainBlocks = img_bytes[10 * 8:]  # decrypt the remaining blocks

        if mode == "ECB":
            decryptedRemainBlocks = ECBDecryption(remainBlocks, key)
        elif mode == "CBC":
            decryptedRemainBlocks = CBCDecryption(remainBlocks, key, IV)

        decrypted_bytes = tenBlocks + decryptedRemainBlocks  # combine unencrypted and decrypted blocks

        expected_length = img.size[0] * img.size[1] * len(img.mode)
        if len(decrypted_bytes) < expected_length:  # Ensure the decrypted bytes length matches the expected length
            decrypted_bytes += b'\x00' * (expected_length - len(decrypted_bytes))  # Pad if it's shorter
        elif len(decrypted_bytes) > expected_length:
            decrypted_bytes = decrypted_bytes[:expected_length]  # Truncate if it's longer

        decrypted_image = Image.frombytes(img.mode, img.size, decrypted_bytes)
        grayscale_decrypted_image = decrypted_image.convert("L")
        grayscale_decrypted_image.show()

        if mode == "ECB":
            grayscale_decrypted_image.save("DecryptedImageECB.png")
        else:
            grayscale_decrypted_image.save("DecryptedImageCBC.png")