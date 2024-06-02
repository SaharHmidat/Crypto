def TEAencryption(plaintext, k, rounds=32, deltaConstant=0x9E3779B9):
    L, R = plaintext
    sum = 0
    for _ in range(rounds):
        sum = (sum + deltaConstant) & 0xFFFFFFFF  # Keep sum within 32 bits
        L = (L + (((R << 4) + k[0]) ^ (R + sum) ^ ((R >> 5) + k[1]))) & 0xFFFFFFFF
        R = (R + (((L << 4) + k[2]) ^ (L + sum) ^ ((L >> 5) + k[3]))) & 0xFFFFFFFF
    return L, R

def TEAdecryption(ciphertext, k, rounds=32, deltaConstant=0x9E3779B9):
    L, R = ciphertext
    sum = (deltaConstant >> 5 ) & 0xFFFFFFFF
    for _ in range(rounds):
        R = (R - (((L << 4) + k[2]) ^ (L + sum) ^ ((L >> 5) + k[3]))) & 0xFFFFFFFF
        L = (L - (((R << 4) + k[0]) ^ (R + sum) ^ ((R >> 5) + k[1]))) & 0xFFFFFFFF
        sum = (sum - deltaConstant) & 0xFFFFFFFF
    return L, R