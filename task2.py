from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        # Open image
        img = Image.open(input_path)
        img = img.convert("RGB")  # Ensure RGB mode
        pixels = img.load()

        width, height = img.size

        # Process pixels
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # XOR each channel with the key
                r_enc = r ^ key
                g_enc = g ^ key
                b_enc = b ^ key

                pixels[x, y] = (r_enc, g_enc, b_enc)

        img.save(output_path)
        print(f"Saved processed image to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Image Encryption Tool ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    input_path = input("Enter image file path: ").strip()
    output_path = input("Enter output file path: ").strip()
    
    try:
        key = int(input("Enter encryption key (0-255): "))
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print("Key must be an integer between 0 and 255.")
        return

    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
