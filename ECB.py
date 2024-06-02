
from TEA import TEAencryption, TEAdecryption
def convertToListInt(data):
    return [int.from_bytes(data[i:i+4], byteorder='big') for i in range(0, len(data), 4)]

def convertToByteString(data):
    return b''.join([x.to_bytes(4, byteorder='big') for x in data])

def lengthInput(data, block_size=8):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unlengthInput(data):
    padding_length = data[-1]
    return data[:-padding_length]

def ECBEncryption(plaintext, key):
    plaintext = lengthInput(plaintext)
    blocks = convertToListInt(plaintext)
    encryptedBlocks = []

    for i in range(0, len(blocks), 2):
        block = (blocks[i], blocks[i + 1])
        encryptedBlock = TEAencryption(block, key)
        encryptedBlocks.extend(encryptedBlock)

    return convertToByteString(encryptedBlocks)

def ECBDecryption(ciphertext, key):
    blocks = convertToListInt(ciphertext)
    decryptedBlocks = []

    for i in range(0, len(blocks), 2):
        block = (blocks[i], blocks[i + 1])
        decryptedBlock = TEAdecryption(block, key)
        decryptedBlocks.extend(decryptedBlock)

    decryptedData = convertToByteString(decryptedBlocks)
    return unlengthInput(decryptedData)


