import os
from PIL import Image

def convert_png_to_jpg(root_folder):
    # Walk through root_folder and its subdirectories.
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".png"):
                png_path = os.path.join(dirpath, filename)
                jpg_path = os.path.join(dirpath, filename[:-4] + ".jpg")
                
                with Image.open(png_path) as img:
                    img = img.convert("RGB")  # Convert the image to RGB mode
                    img.save(jpg_path, "JPEG")

if __name__ == "__main__":
    root_folder = "./"
    convert_png_to_jpg(root_folder)
