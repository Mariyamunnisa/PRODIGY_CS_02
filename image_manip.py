from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
   
    # Convert image to RGB mode
    img_rgb = img.convert('RGB')
   
    # Create a new image for encryption
    encrypted_img = Image.new('RGB', (width, height))
   
    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img_rgb.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_img.putpixel((x, y), (r, g, b))
   
    # Save the encrypted image
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size
   
    # Create a new image for decryption
    decrypted_img = Image.new('RGB', (width, height))
   
    # Decrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_img.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_img.putpixel((x, y), (r, g, b))
   
    # Save the decrypted image
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted successfully!")

# Example usage
image_path = '/home/mariyam/Desktop/IMG_20230629_181950.jpg'
key = 50
encrypt_image(image_path, key)
decrypt_image('encrypted_image.png', key)


