import math
import json
import srt
import pickle
from backend.speech_bubble.lip_detection import get_lips
from backend.speech_bubble.bubble_placement import get_bubble_position

page_template = ['142344', '312341', '312341', '4432111', '312341', '131423', '142344', '67']

class bubble:

    def __init__(self,bubble_offset_x,bubble_offset_y,lip_x,lip_y,dialog):

        bubble_width=200
        bubble_height=94
        tail_centre_x=100
        tail_centre_y=47
        self.dialog = dialog

        self.bubble_offset_x = bubble_offset_x
        self.bubble_offset_y = bubble_offset_y
        
        temp = math.degrees(math.atan((bubble_offset_x-lip_x)/(bubble_offset_y-lip_y)))

        if(bubble_offset_y>lip_y):
            # tail top
            if(bubble_offset_x>lip_x):
                #tail left
                angle=180-temp
            elif(bubble_offset_x<lip_x):
                #tail right
                angle=180-temp
        elif(bubble_offset_y<lip_y):
            #tail bottom
            if(bubble_offset_x>lip_x):
                #tail left
                angle=-temp
            elif(bubble_offset_x<lip_x):
                #tail right
                angle=360-temp

        if(bubble_offset_x==lip_x):
            angle=0
            if(bubble_offset_y>lip_y):
                angle=180
            if(bubble_offset_y<lip_y):
                angle=0

        print(angle)

        self.tail_deg=angle

        if(bubble_offset_y>lip_y):
            # tail top
            if(bubble_offset_x>lip_x):
                #tail left
                tail_offset_x=tail_centre_x-50
                tail_offset_y=tail_centre_y-23
            elif(bubble_offset_x<lip_x):
                #tail right
                tail_offset_x=tail_centre_x+50
                tail_offset_y=tail_centre_y-23
        elif(bubble_offset_y<lip_y):
            #tail bottom
            if(bubble_offset_x>lip_x):
                #tail left
                tail_offset_x=tail_centre_x-50
                tail_offset_y=tail_centre_y+23
            elif(bubble_offset_x<lip_x):
                #tail right
                tail_offset_x=tail_centre_x+50
                tail_offset_y=tail_centre_y+23
        
        if(bubble_offset_x==lip_x):
            tail_offset_x=tail_centre_x
            if(bubble_offset_y>lip_y):
                tail_offset_y=tail_centre_y-23
            if(bubble_offset_y<lip_y):
                tail_offset_y=tail_centre_y+23


        self.tail_offset_x = tail_offset_x
        self.tail_offset_y = tail_offset_y


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

    with open('bubble.js', 'w') as f:
        f.write(f'var page_template = {page_template}')
        f.write("\n var bubble = ")

    f.close()

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
        bubbles.append(temp.__dict__)


    with open('bubble.js', 'a') as f:
        json.dump(bubbles, f , indent=4)
    f.close()









