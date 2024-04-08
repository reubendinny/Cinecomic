import math
import numpy as np
class panel:
    def __init__(self,image,row_span,col_span):
       self.image = image
       self.row_span = row_span
       self.col_span = col_span


# class bubble:

#     def __init__(self,bubble_offset_x,bubble_offset_y,lip_x,lip_y,dialog):

#         bubble_width=200
#         bubble_height=94
#         tail_centre_x=100
#         tail_centre_y=47
#         self.dialog = dialog

#         self.bubble_offset_x = bubble_offset_x
#         self.bubble_offset_y = bubble_offset_y
        
#         temp = 0
#         angle = 0
#         try:
#             temp = math.degrees(math.atan((bubble_offset_y-lip_y) / (bubble_offset_x-lip_x)))
#         except ZeroDivisionError:
#             temp = 45

#         if(bubble_offset_y>lip_y):
#             # tail top
#             if(bubble_offset_x>lip_x):
#                 #tail left
#                 angle=180-temp
#             elif(bubble_offset_x<lip_x):
#                 #tail right
#                 angle=180-temp
#         elif(bubble_offset_y<=lip_y):
#             #tail bottom
#             if(bubble_offset_x>lip_x):
#                 #tail left
#                 angle=-temp
#             elif(bubble_offset_x<lip_x):
#                 #tail right
#                 angle=360-temp

#         print(angle)
#         tail_offset_x = None
#         tail_offset_y = None

#         self.tail_deg=angle

#         if(bubble_offset_y>lip_y):
#             # tail top
#             if(bubble_offset_x>lip_x):
#                 #tail left
#                 tail_offset_x=tail_centre_x-50
#                 tail_offset_y=tail_centre_y-23
#             elif(bubble_offset_x<lip_x):
#                 #tail right
#                 tail_offset_x=tail_centre_x+50
#                 tail_offset_y=tail_centre_y-23
#         elif(bubble_offset_y<=lip_y):
#             #tail bottom
#             if(bubble_offset_x>lip_x):
#                 #tail left
#                 tail_offset_x=tail_centre_x-50
#                 tail_offset_y=tail_centre_y+23
#             elif(bubble_offset_x<lip_x):
#                 #tail right
#                 tail_offset_x=tail_centre_x+50
#                 tail_offset_y=tail_centre_y+23

#         self.tail_offset_x = tail_offset_x
#         self.tail_offset_y = tail_offset_y

class bubble:

    def __init__(self,bubble_offset_x,bubble_offset_y,lip_x,lip_y,dialog):

        bubble_width=200
        bubble_height=94
        tail_centre_x=100
        tail_centre_y=47
        self.dialog = dialog

        self.bubble_offset_x = bubble_offset_x
        self.bubble_offset_y = bubble_offset_y
        
        temp = 0
        angle = 0

        dx = lip_x - bubble_offset_x
        dy = lip_y - bubble_offset_y
        # hyp = np.hypot(dx,dy) 

        angle = np.arctan2(dy, dx)
        print(angle)

        tail_offset_x = None
        tail_offset_y = None

        self.tail_deg=np.degrees(angle)

        self.tail_offset_x = tail_centre_x * np.cos(angle)
        self.tail_offset_y = tail_centre_x * np.sin(angle)

        dx = lip_x - bubble_offset_x+self.tail_offset_x
        dy = lip_y - bubble_offset_y+self.tail_offset_y

        new_angle = np.arctan2(dy, dx)
        self.tail_deg = np.degrees(angle)
        # if(bubble_offset_y>lip_y):
        #     # tail top
        #     if(bubble_offset_x>lip_x):
        #         #tail left
        #         tail_offset_x=tail_centre_x-50
        #         tail_offset_y=tail_centre_y-23
        #     elif(bubble_offset_x<lip_x):
        #         #tail right
        #         tail_offset_x=tail_centre_x+50
        #         tail_offset_y=tail_centre_y-23
        # elif(bubble_offset_y<=lip_y):
        #     #tail bottom
        #     if(bubble_offset_x>lip_x):
        #         #tail left
        #         tail_offset_x=tail_centre_x-50
        #         tail_offset_y=tail_centre_y+23
        #     elif(bubble_offset_x<lip_x):
        #         #tail right
        #         tail_offset_x=tail_centre_x+50
        #         tail_offset_y=tail_centre_y+23





# page.py

class Page:
    def __init__(self,panels,bubbles):
        self.panels = []
        self.bubbles = []

        for i in range(len(panels)):
            self.panels.append(panels[i].__dict__)
            self.bubbles.append(bubbles[i].__dict__)