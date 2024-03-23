import math
import json

class bubble:
    def __init__(self,bubble_offset_x,bubble_offset_y,lip_x,lip_y):
        self.bubble_offset_x = bubble_offset_x
        self.bubble_offset_y = bubble_offset_y
        self.lip_x = lip_x
        self.lip_y = lip_y

        temp = 
        self.tail_deg = math.degrees(math.atan((bubble_offset_x-lip_x)/(bubble_offset_y-lip_y)))


b1 = bubble(3,4,11,1)
b2 = bubble(0,0,11,3)


print(b1.__dict__)
print(b2.__dict__)

    


