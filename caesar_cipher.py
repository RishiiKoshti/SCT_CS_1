def caesar_cipher(text, shift, mode):
    result = ""
    if mode.lower() == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("--- Caesar Cipher Program ---")
    while True:
        mode = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit?: ").strip().lower()
        
        if mode in ['q', 'quit']:
            print("Goodbye!")
            break
        elif mode in ['e', 'encrypt']:
            action = 'encrypt'
        elif mode in ['d', 'decrypt']:
            action = 'decrypt'
        else:
            print("Invalid choice. Please choose E, D, or Q.")
            continue
            
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Please enter a valid integer for the shift value.\n")
            continue
            
        output = caesar_cipher(message, shift, action)
        print(f"\nResult ({action}ed): {output}\n")
        print("-" * 30)

if __name__ == "__main__":
    main()