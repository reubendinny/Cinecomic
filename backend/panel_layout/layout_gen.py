
import os
from os import listdir
from backend.panel_layout.cam import get_coordinates
from backend.utils import crop_image
from backend.panel_layout.layout.page import get_templates,insert_in_grid


# Dimensions of the entire page
hT = 1654
wT = 1169

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
    }
}

# print(type1,type2,type3,type4)

def get_panel_type(left,right,top,bottom):
    w = right - left
    h = bottom - top
    aspect_ratio = w/h

    if 0 <= aspect_ratio < 0.75:
        return '2'
    elif 0.75 <= aspect_ratio < 1.25:
        return '1'
    elif 1.25 <= aspect_ratio < 2.25:
        return '4'
    else:
        return '3'

def centroid_crop(index, panel_type, cam_coords):
    left, right, top, bottom = cam_coords[0], cam_coords[1], cam_coords[2], cam_coords[3]

    xC, yC = (right + left)/2, (bottom + top)/2
    
    print("camcoords: ",left,right,top,bottom)
    # ======================MODIFIED=======================================================================
    w, h = right-left, bottom-top
    wP, hP = types[panel_type]['width'], types[panel_type]['height']

    if wP < hP:
        S = h / hP
        new_width = wP * S
        crop_left = xC - (new_width/2)
        crop_right = xC + (new_width/2)
        crop_top = top
        crop_bottom = bottom

    else:
        S = w / wP
        new_height = hP * S
        crop_top = yC - (new_height/2)
        crop_bottom = yC + (new_height/2)
        crop_left = left
        crop_right = right
  

    # resolve edge condition also --> If coordinates exceeds image coordinates, scale down the coordinates
        # resolved in crop utils
    
    # ======================MODIFIED=======================================================================

    # # Place panel wrt the centroid
    # crop_left = xC - (0.5 * types[panel_type]['width']) 
    # crop_right = xC + (0.5 * types[panel_type]['width']) 
    # crop_top = yC - (0.5 * types[panel_type]['height']) 
    # crop_bottom = yC + (0.5 * types[panel_type]['height']) 

    # # Scale the panel to fit the bounding box 
    # # if(panel_type == '2'):
    # #     Sfactor =  (right - left) / types[panel_type]['width']
    # # else:
    # Sfactor = (bottom - top) / types[panel_type]['height']

    # xCcrop, yCcrop = (crop_right - crop_left)/2, (crop_bottom - crop_top)/2

    # # if Sfactor >= 1:
    # crop_left = xCcrop - ((xCcrop - crop_left) * Sfactor)
    # crop_right = xCcrop + ((crop_right - xCcrop) * Sfactor)
    # crop_top = yCcrop + ((crop_top - yCcrop) * Sfactor)
    # crop_bottom = yCcrop - ((yCcrop - crop_bottom) * Sfactor)
    # # else:
    # #     crop_left = xCcrop + ((xCcrop - crop_left) * Sfactor)
    # #     crop_right = xCcrop - ((crop_right - xCcrop) * Sfactor)
    # #     crop_top = yCcrop - ((crop_top - yCcrop) * Sfactor)
    # #     crop_bottom = yCcrop + ((yCcrop - crop_bottom) * Sfactor)

    # Crop image
    frame_path = os.path.join("frames",'final',f"frame{index+1:03d}.png")
    
    print("crop1coords: ", crop_left,crop_right,crop_top, crop_bottom)
    crop_image(frame_path, crop_left,crop_right,crop_top, crop_bottom)

def generate_layout():
    input_seq = ""
    cam_coords = []

    # Loop through images and get type
    folder_dir = "frames/final"
    for image in os.listdir(folder_dir):

        frame_path = os.path.join("frames",'final',image)
        left, right, top, bottom = get_coordinates(frame_path)
        input_seq += get_panel_type(left, right, top, bottom)
        # print(left, right, top, bottom)

        cam_coords.append((left, right, top, bottom))
    
    page_templates = get_templates(input_seq)
    print(page_templates)
    i = 0
    try:
        for page in page_templates:
            for panel in page:
                centroid_crop(i, panel, cam_coords[i])
                i += 1
    except(IndexError):
        pass


    insert_in_grid(page_templates)


        



