import shutil
import os
from PIL import Image

def copy_and_rename_file(source_file, destination_folder, new_file_name):

    destination_path = os.path.join(destination_folder, new_file_name)

    try:
        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            os.remove(destination_path)  # Remove the existing file
            
        # Copy the file from source to destination
        shutil.copy(source_file, destination_path)
        os.rename(destination_path, os.path.join(destination_folder, new_file_name))

        
        print(f"File '{source_file}' copied and renamed to '{new_file_name}' in '{destination_folder}'.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

def crop_image(img_path, left, right, top, bottom):
    img = Image.open(img_path)
    width, height = img.size

    
    # Reposition if it exceeds image boundary
    new_left, new_right, new_top, new_bottom = left, right, top, bottom
    if(left < 0):
        new_left = left + (-left) 
        new_right = right + -(left)

    if(right > width):
        new_left = left - (right-width)
        new_right = right - (right-width)

    if(top < 0):
        new_top = top + -(top)
        new_bottom = bottom + -(top)

    if(bottom > height):
        new_top = top - (bottom-height)
        new_bottom = bottom - (bottom-height)
    
    # Crop the image wrt the 4 coordinates
    box = (new_left, new_top, new_right, new_bottom)
    img2 = img.crop(box)
    
    # Save the cropped image
    img2.save(img_path)

    # img2.show()
    # return img2