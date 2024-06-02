from ECB import lengthInput, convertToListInt, convertToByteString, unlengthInput
from TEA import TEAencryption, TEAdecryption


def CBCEncryption(plaintext, key, IV):
    plaintext = lengthInput(plaintext)
    blocks = convertToListInt(plaintext)
    encryptedBlocks = []
    IV = convertToListInt(IV)
    previousBlock = IV

    for i in range(0, len(blocks), 2):
        block = (blocks[i], blocks[i + 1])
        block = (block[0] ^ previousBlock[0], block[1] ^ previousBlock[1])
        encryptedBlock = TEAencryption(block, key)
        encryptedBlocks.extend(encryptedBlock)
        previousBlock = encryptedBlock

    return convertToByteString(encryptedBlocks)

def CBCDecryption(cipherText, key, IV):
    blocks = convertToListInt(cipherText)
    decryptedBlocks = []

    IV = convertToListInt(IV)
    previousBlock = IV

    for i in range(0, len(blocks), 2):
        block = (blocks[i], blocks[i + 1])
        decryptedBlock = TEAdecryption(block, key)
        decryptedBlock = (decryptedBlock[0] ^ previousBlock[0], decryptedBlock[1] ^ previousBlock[1])
        decryptedBlocks.extend(decryptedBlock)
        previousBlock = block

    decryptedData = convertToByteString(decryptedBlocks)
    return unlengthInput(decryptedData)