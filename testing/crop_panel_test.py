from PIL import Image

# Dimensions of the entire page
# hT = 1100
# wT = 1000

#Dimensions of a panel
# hP = hT/3
# wP = wT/4

# # Defining aspect ratios
# type1 = wP/hP
# type2 = wP/(2*hP)
# type3 = (3*wP)/hP
# type4 = (2*wP)/hP
# print(type1,type2,type3,type4)

def get_panel_type(left,right,top,bottom):
    x_ = (right-left)/2
    y_ = (bottom-top)/2

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
    
print(get_panel_type(0,507,0,1077))





