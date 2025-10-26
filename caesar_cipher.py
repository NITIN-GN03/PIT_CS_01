# Caesar Cipher Implementation

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"\nEncrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
