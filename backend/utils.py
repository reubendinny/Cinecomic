import shutil
import os
from PIL import Image
import cv2
import numpy as np

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

def get_black_bar_coordinates(img_path):
    image = cv2.imread(img_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(image_gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour with four corners
    largest_contour = np.array([])
    max_area = 0
    for cntrs in contours:
        area = cv2.contourArea(cntrs)
        peri = cv2.arcLength(cntrs, True)
        approx = cv2.approxPolyDP(cntrs, 0.02 * peri, True)
        if area > max_area:
            largest_contour = approx
            max_area = area

    # Extract bounding box
    x, y, w, h = cv2.boundingRect(largest_contour)
    print("Black bar coords : ", x,y,w,h)
    return x, y, w, h

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
    return (new_left, new_right, new_top, new_bottom)
    # img2.show()
    # return img2