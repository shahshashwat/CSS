def encrypt(text, key):
    result = ""
    for l in text:
        if l.isupper():
            result += chr((ord(l)+key-65)%26 + 65)
        elif l.islower():
            result += chr((ord(l)+key-97)%26 + 97)
        else:
            result += l
    return result
    
    
def decrypt(text, key):
    result = ""
    for l in text:
        if l.isupper():
            result += chr((ord(l)-key-65)%26 + 65)
        elif l.islower():
            result += chr((ord(l)-key-97)%26 + 97)
        else:
            result += l
    return result
    
    
text = "Work hard"
key = 1
e = encrypt(text, key)
d = decrypt(e, key)
print(f"Encryption: {e}")
print(f"Decryption {d}")