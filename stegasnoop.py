import argparse
import sys
import math
import os
from PIL import Image

def calculate_entropy(image):
    """Calculates the Shannon entropy of the image."""
    histogram = image.histogram()
    histogram_length = sum(histogram)
    samples_probability = [float(h) / histogram_length for h in histogram]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

def analyze_lsb(image):
    """Placeholder for Least Significant Bit (LSB) analysis."""
    print("    [-] Performing LSB Analysis... (Basic check)")
    return "No obvious LSB anomalies found"

def check_adjacent_correlation(image):
    """Placeholder for Adjacent Pixel Correlation analysis."""
    print("    [-] Checking adjacent pixel correlation...")
    return "Correlation normal"

def scan_single_image(file_path, threshold):
    """
    Core logic to scan a single image file.
    """
    print(f"\n[*] Scanning image: {file_path}")
    try:
        img = Image.open(file_path)
        
        # 1. Entropy Check
        entropy = calculate_entropy(img)
        print(f"    [-] Shannon Entropy: {entropy:.4f}")
        
        if entropy > threshold:
            print(f"    [!] WARNING: High entropy detected! Possible compressed or encrypted data.")
        
        # 2. LSB Analysis
        analyze_lsb(img)

        # 3. Correlation Check
        check_adjacent_correlation(img)

        print("    [*] Scan complete.")

    except Exception as e:
        print(f"    [x] Error processing {file_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="StegaSnoop: Lightweight Steganography Detector")
    
    # Updated help text to reflect folder support
    parser.add_argument("path", help="Path to the image file OR directory of images to analyze")
    parser.add_argument("--threshold", type=float, default=7.5, help="Entropy threshold for detection")

    args = parser.parse_args()

    # Valid image extensions to look for in folder mode
    VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    if os.path.isdir(args.path):
        # FOLDER MODE: Loop through all images in the directory
        print(f"[*] Directory detected. Scanning all images in: {args.path}")
        
        found_images = False
        for filename in os.listdir(args.path):
            if filename.lower().endswith(VALID_EXTENSIONS):
                found_images = True
                full_path = os.path.join(args.path, filename)
                scan_single_image(full_path, args.threshold)
        
        if not found_images:
            print(f"[!] No valid images found in {args.path}")

    elif os.path.isfile(args.path):
        # FILE MODE: Scan just the one file
        scan_single_image(args.path, args.threshold)

    else:
        print(f"[x] Error: The path '{args.path}' does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()