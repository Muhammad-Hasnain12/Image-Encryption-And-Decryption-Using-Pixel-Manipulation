from PIL import Image
import os

def encrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (g, b, r)  # Swapping red and green values
    
    save_path = os.path.join(os.path.dirname(image_path), "encrypted_image.png")
    img.save(save_path)
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path)
    pixels = img.load()
    
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # Example operation: reversing the encryption (swapping pixel values back)
            g, b, r = pixels[x, y]
            pixels[x, y] = (r, g, b)  # Swapping green and red values
    
    # Save the decrypted image
    save_path = os.path.join(os.path.dirname(encrypted_image_path), "decrypted_image.png")
    img.save(save_path)
    print("Image decrypted successfully!")

# Usage example:
# Encrypt an image
input_image_path = r"C:\Users\Hasnain's PC\Desktop\PRODIGY INFOTECH\input_image.png"
encrypt_image(input_image_path)

# Decrypt the encrypted image
encrypted_image_path = r"C:\Users\Hasnain's PC\Desktop\PRODIGY INFOTECH\encrypted_image.png"
decrypt_image(encrypted_image_path)