import os
import subprocess

def convert_image_with_bc1(input_path, bc1_batch_file):
    """Convert a single image file using the BC1 batch file."""
    output_path = os.path.splitext(input_path)[0] + ".dds"
    
    # Run the BC1 batch file
    result = subprocess.run([bc1_batch_file, input_path], shell=True, capture_output=True, text=True)
    
    # Log the output
    print(f"Processing {input_path}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    if result.returncode == 0:
        print(f"Conversion successful: {input_path} -> {output_path}")
    else:
        print(f"Conversion failed: {input_path}")

def convert_images_recursive(root_directory, bc1_batch_file):
    """Recursively convert images in all subdirectories using BC1."""
    for subdir, _, files in os.walk(root_directory):
        for filename in files:
            if filename.lower().endswith(".png"):
                input_path = os.path.join(subdir, filename)
                convert_image_with_bc1(input_path, bc1_batch_file)

if __name__ == "__main__":
    # Define the batch file path
    bc1_batch_file = r"C:\<PATH>\convert_to_dds.bat"  # Replace with the actual path to your BC1 batch file
    
    # Set the directory containing your PNG files
    root_directory = r"C:\<PATH>\textures"  # Replace with the actual path to your images directory
    
    convert_images_recursive(root_directory, bc1_batch_file)