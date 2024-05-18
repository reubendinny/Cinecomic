import shutil
import os
from PIL import Image
import cv2
import numpy as np
import yt_dlp
import re

# Dimensions of the entire page
hT = 1100
wT = 1035

# Dimensions of a panel
hP = hT/3
wP = wT/4

# Defining types
types = {
    '1': {
        "width" : wP,
        "height" : hP,
        "aspect_ratio" : wP/hP
    },

    '2': {
        "width" : wP,
        "height" : 2*hP,
        "aspect_ratio" : wP/(2*hP)
    },

    '3': {
        "width" : 3*wP,
        "height" : hP,
        "aspect_ratio" : (3*wP)/hP
    },

    '4': {
        "width" : 2*wP,
        "height" : hP,
        "aspect_ratio" : (2*wP)/hP
    },

    '5':{
        "width" : 4*wP,
        "height" : 3*hP,
        "aspect_ratio" : (4*wP)/(3*hP)
    },

    '6':{
        "width" : 4*wP,
        "height" : hP,
        "aspect_ratio" : (4*wP)/hP
    },

    '7':{
        "width" : 4*wP,
        "height" : 2*hP,
        "aspect_ratio" : (4*wP)/(2*hP)
    },

    '8':{
        "width" : 2*wP,
        "height" : 2*hP,
        "aspect_ratio" : (2*wP)/(2*hP)
    }
}

def get_panel_type(left,right,top,bottom):
    w = right - left
    h = bottom - top
    aspect_ratio = w/h

    if 0 <= aspect_ratio < 0.7:
        return '2'
    elif 0.7 <= aspect_ratio < 1.4:
        return '1'
    elif 1.4 <= aspect_ratio < 2:
        return '4'
    else:
        return '3'

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

def convert_to_css_pixel(x,y,crop_coord):
    #Scaling the image to CSS pixels. DPI : (1px/1 css px)
    left, right, top, bottom = crop_coord
    panel_type = get_panel_type(left, right, top, bottom)
    panel_width = types[panel_type]['width']
    image_width = right-left
    dpi_width = image_width/panel_width

    panel_height = types[panel_type]['height']
    # print("Panel Height:",panel_height)
    image_height = bottom-top
    dpi_height = image_height/panel_height
    # print("DPI Height",dpi_height)

    x /= dpi_width
    y /= dpi_height
    return x,y

def clear_folder(folder_path):
    """Delete all contents of a folder but not the folder itself."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def delete_other_folders(base_path, exclude_folder):
    """Delete all folders within base_path except the exclude_folder."""
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path) and folder_name != exclude_folder:
            try:
                shutil.rmtree(folder_path)
            except Exception as e:
                print(f'Failed to delete {folder_path}. Reason: {e}')

def cleanup():
    frames_path = 'frames'
    final_folder_name = 'final'
    final_folder_path = os.path.join(frames_path, final_folder_name)
    uploaded_video_path = os.path.join('video', 'uploaded.mp4')

    os.makedirs(final_folder_path, exist_ok=True) # If folders does not exist, create:
    os.makedirs('video', exist_ok=True)

    # Clear the contents of the final folder
    if os.path.exists(final_folder_path):
        clear_folder(final_folder_path)
        print("Deleting previous frames")
    else:
        print(f'The folder {final_folder_path} does not exist.')

    # Delete all other folders in the frames folder
    delete_other_folders(frames_path, final_folder_name)

    # Deleting the uploaded.mp4
    if os.path.exists(uploaded_video_path):
        os.remove(uploaded_video_path)
        print(f"Previous video deleted successfully")
        
    print("Deleted previous sub folders")

def download_video(url):
    print("Downloading video")
    ydl_opts = {
        'outtmpl': f'video/uploaded.%(ext)s',
        'format': f'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]/best[height<=1080]'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def convert_to_embed(url):
    # Regular expression to capture the video ID from the YouTube URL
    video_id_pattern = re.compile(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*")
    match = video_id_pattern.search(url)
    
    if not match:
        return None  # Return None if no video ID is found
    
    video_id = match.group(1)
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    return embed_url
