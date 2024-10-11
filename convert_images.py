import os
import subprocess
import warnings
from PIL import Image

# Suppress DecompressionBombWarning
warnings.simplefilter('ignore', Image.DecompressionBombWarning)

def has_transparency(img):
    """Check if the image has transparency."""
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False

def convert_images(directory):
    # Define the batch file paths
    bc3_batch_file = r"C:\<PATH>\convert_to_dds_alpha.bat"  # Replace with the actual path to your BC3 batch file
    bc1_batch_file = r"C:\<PATH>\convert_to_dds.bat"  # Replace with the actual path to your BC1 batch file
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.splitext(input_path)[0] + ".dds"
            
            # Open the image file to check for transparency
            with Image.open(input_path) as img:
                if has_transparency(img):
                    batch_file = bc3_batch_file
                else:
                    batch_file = bc1_batch_file
            
            # Run the chosen batch file
            result = subprocess.run([batch_file, input_path], shell=True, capture_output=True, text=True)
            
            # Log the output
            print(f"Processing {input_path}")
            print(f"STDOUT:\n{result.stdout}")
            print(f"STDERR:\n{result.stderr}")
            
            if result.returncode == 0:
                print(f"Conversion successful: {input_path} -> {output_path}")
            else:
                print(f"Conversion failed: {input_path}")

if __name__ == "__main__":
    # Set the directory containing your PNG files
    directory = r"C:\<PATH>\textures\"  # Replace with the actual path to your images directory
    convert_images(directory)