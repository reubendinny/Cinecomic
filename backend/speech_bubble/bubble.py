import math
import json
import srt


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
with open("test1.srt") as f:
    data=f.read()

subs=srt.parse(data)
file = open('bubble.js', 'a')

bubbles = []
for sub in subs:
    temp = bubble(4,1,2,2,sub.content)
    bubbles.append(temp)

    # convert into JSON:
    y = json.dumps(temp.__dict__)

    # the result is a JSON string:
    print(y)
    file.write(y)
file.close()


for b in bubbles:
    print(b.__dict__)







