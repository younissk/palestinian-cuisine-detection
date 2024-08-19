import glob
import os
import shutil
from PIL import Image


image_folders = glob.glob("images/*")

print(image_folders)

valid_images = []

for folder in image_folders:
    print("=================================================================")
    images = glob.glob(folder + "/*")
    
    # Check if the image is a valid image, some might be corrupted
    print(f"Checking {folder} for valid images")
    for image in images:
        try:
            Image.open(image)
        except:
            print(f"Invalid image: {image}")
            os.remove(image)
            print(f"Removed image: {image}")
            continue
        valid_images.append(image)
        print(f"Valid image: {image}")
    
    print(f"Found {len(valid_images)} valid images in {folder}")
    
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for image in valid_images:
    shutil.copy(image, output_folder)

print(f"Copied {len(valid_images)} valid images to {output_folder}")