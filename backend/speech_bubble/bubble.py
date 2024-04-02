import math
import json
import srt

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

        self.tail_offset_x = tail_offset_x
        self.tail_offset_y = tail_offset_y

data=""
with open("./../../test1.srt") as f:
    data=f.read()

subs=srt.parse(data)

bubbles = []


for sub in subs:
    temp = bubble(4,1,2,2,sub.content)
    bubbles.append(temp.__dict__)


with open('data.json', 'w') as f:
    json.dump(bubbles, f)









