from PIL import Image
import os

def process_image(image_path, key, mode):
    try:
        # Open the image and convert it to RGB mode
        img = Image.open(image_path)
        rgb_img = img.convert('RGB')
        pixels = rgb_img.load()
        
        width, height = rgb_img.size
        
        # Loop through every single pixel row by row
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                if mode == 'encrypt':
                    # Apply a basic mathematical operation (XOR with key)
                    # Using modulo 256 ensures values stay within 0-255 RGB limits
                    new_r = (r ^ key) % 256
                    new_g = (g ^ key) % 256
                    new_b = (b ^ key) % 256
                else: # decrypt
                    # XOR is its own inverse, so the same math reverses it
                    new_r = (r ^ key) % 256
                    new_g = (g ^ key) % 256
                    new_b = (b ^ key) % 256
                    
                pixels[x, y] = (new_r, new_g, new_b)
        
        # Create output filename
        dir_name, file_name = os.path.split(image_path)
        output_path = os.path.join(dir_name, f"{mode}ed_{file_name}")
        
        # Save the altered image
        rgb_img.save(output_path)
        print(f"\n[Success] Image successfully {mode}ed and saved to: {output_path}")
        
    except Exception as e:
        print(f"[Error] Could not process image: {e}")

def main():
    print("--- Pixel Manipulation Image Encryption Tool ---")
    
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit?: ").strip().lower()
        
        if choice in ['q', 'quit']:
            print("Goodbye!")
            break
        elif choice in ['e', 'encrypt']:
            mode = 'encrypt'
        elif choice in ['d', 'decrypt']:
            mode = 'decrypt'
        else:
            print("Invalid choice. Select E, D, or Q.")
            continue
            
        img_path = input("Enter the absolute image file path: ").strip().strip('"')
        
        if not os.path.exists(img_path):
            print("Error: File does not exist. Please check the path.\n")
            continue
            
        try:
            key = int(input("Enter an encryption key (integer from 1-255): "))
            if not (1 <= key <= 255):
                print("Please keep the key between 1 and 255 for best results.")
                continue
        except ValueError:
            print("Invalid key format. Must be an integer.\n")
            continue
            
        process_image(img_path, key, mode)
        print("-" * 40)

if __name__ == "__main__":
    main()