def caesar_encrypt(text, k):
    ciphertext = ""
    k = k % 26  
    for char in text:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + k) % 26 + base)
        else:
            ciphertext += char 
    return ciphertext

plaintext = "Pham Thi Anh Tho"
k = 53 
ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("Key (k)   :", k, "≡", k % 26, "(mod 26)")
print("Ciphertext:", ciphertext)
