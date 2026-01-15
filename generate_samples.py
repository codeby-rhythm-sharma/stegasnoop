from PIL import Image
import random
import os

def create_samples():
    # Create a directory for the samples if it doesn't exist
    if not os.path.exists("examples"):
        os.makedirs("examples")

    print("[*] Generating sample images...")

    # 1. Create a "Clean" Image (Low Entropy)
    # A simple gradient has very predictable data (low entropy)
    clean_img = Image.new("RGB", (200, 200))
    pixels = clean_img.load()
    for x in range(200):
        for y in range(200):
            # Smooth gradient
            pixels[x, y] = (x, y, 100) 
    
    clean_img.save("examples/clean_sample.png")
    print("  -> Created examples/clean_sample.png (Low Entropy)")

    # 2. Create a "Suspicious" Image (High Entropy)
    # Random noise mimics encrypted data or heavy steganography
    suspicious_img = Image.new("RGB", (200, 200))
    pixels = suspicious_img.load()
    for x in range(200):
        for y in range(200):
            # Complete random noise
            pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    suspicious_img.save("examples/suspicious_sample.png")
    print("  -> Created examples/suspicious_sample.png (High Entropy)")

if __name__ == "__main__":
    create_samples()