import os
from os import listdir
from backend.panel_layout.cam import get_coordinates, dump_CAM_data
from backend.utils import crop_image
from backend.panel_layout.layout.page import get_templates,panel_create
from backend.utils import get_panel_type, types
from PIL import Image


def centroid_crop(index, panel_type, cam_coords, img_w, img_h):
    left, right, top, bottom, yC, xC = cam_coords[0], cam_coords[1], cam_coords[2], cam_coords[3], cam_coords[4], cam_coords[5]
    # xC, yC = (right + left)/2, (bottom + top)/2
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
    
    print("First: ", crop_left,crop_right,crop_top, crop_bottom)
    
    # Scale down if it exceeds image boundary
    if crop_right - crop_left > img_w :
        crop_w = crop_right - crop_left
        crop_h = crop_bottom - crop_top
        S = img_w / crop_w

        new_width = S * crop_w 
        new_height = S * crop_h

        crop_left = xC - (new_width/2)
        crop_right = xC + (new_width/2)
        crop_top = yC - (new_height/2)
        crop_bottom = yC + (new_height/2)

    elif crop_bottom - crop_top > img_h:
        crop_w = crop_right - crop_left
        crop_h = crop_bottom - crop_top
        S = img_h / crop_h

        new_width = S * crop_w 
        new_height = S * crop_h

        crop_left = xC - (new_width/2)
        crop_right = xC + (new_width/2)
        crop_top = yC - (new_height/2)
        crop_bottom = yC + (new_height/2)
    print("Scaled down ", crop_left,crop_right,crop_top, crop_bottom)
        
    # Crop image
    frame_path = os.path.join("frames",'final',f"frame{index+1:03d}.png")
    crop_coords = crop_image(frame_path, crop_left,crop_right,crop_top, crop_bottom)
    return crop_coords


def generate_layout():
    input_seq = ""
    cam_coords = []
    #Get dimensions of images
    img = Image.open(os.path.join("frames",'final',f"frame001.png"))
    width, height = img.size
    
    # Loop through images and get type
    folder_dir = "frames/final"
    for image in os.listdir(folder_dir):

        frame_path = os.path.join("frames",'final',image)
        left, right, top, bottom, center_x, center_y = get_coordinates(frame_path)
        input_seq += get_panel_type(left, right, top, bottom)

        cam_coords.append((left, right, top, bottom, center_x, center_y))
    
    page_templates = get_templates(input_seq)
    print(page_templates)
    i = 0
    crop_coords = []
    try:
        for page in page_templates:
            for panel in page:
                origin = centroid_crop(i, panel, cam_coords[i], width, height)
                crop_coords.append(origin)
                i += 1
    except(IndexError):
        pass

    panels = panel_create(page_templates)
    dump_CAM_data()
    return crop_coords, page_templates, panels