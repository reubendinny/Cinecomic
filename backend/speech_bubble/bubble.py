import math
import json
import srt
import pickle
from backend.speech_bubble.lip_detection import get_lips
from backend.speech_bubble.bubble_placement import get_bubble_position
from backend.class_def import bubble


def bubble_create(video, crop_coords, black_x, black_y):

    bubbles = []

    # def bubble_create(bubble_cord,lip_cord,page_template):
    data=""
    with open("test1.srt") as f:
        data=f.read()
    subs=srt.parse(data)

    # Reading CAM data from dump
    CAM_data = None
    with open('CAM_data.pkl', 'rb') as f:
        CAM_data = pickle.load(f)



    lips = get_lips(video, crop_coords,black_x,black_y)
    
    for sub in subs:
        lip_x = lips[sub.index][0]
        lip_y = lips[sub.index][1]

        bubble_x, bubble_y = get_bubble_position(crop_coords[sub.index-1], CAM_data[sub.index-1])
        # If lip wasn't detected
        if lip_x == -1 and lip_y == -1:
            lip_x = 0
            lip_y = 0

        temp = bubble(bubble_x, bubble_y,lip_x,lip_y,sub.content)
        bubbles.append(temp)


    return bubbles









