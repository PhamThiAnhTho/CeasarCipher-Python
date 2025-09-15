def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + k) % 26 + base)
        else:
            ciphertext += char
    return ciphertext

if __name__ == "__main__":
    stt = 44
    k = stt % 26  
    plaintext = "PhamThiAnhTho"
    ciphertext = caesar_encrypt(plaintext, k)
    
    print(f"Plaintext : {plaintext}")
    print(f"STT       : {stt}")
    print(f"Key (k)   : {k}")
    print(f"Ciphertext: {ciphertext}")
