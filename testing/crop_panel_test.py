# Dimensions of the entire page
hT = 1100
wT = 1000

#Dimensions of a panel
hP = hT/3
wP = wT/4

# Defining aspect ratios
type1 = wP/hP
type2 = wP/(2*hP)
type3 = (3*wP)/hP
type4 = (2*wP)/hP
print(type1,type2,type3,type4)

def get_panel_type(left,right,top,bottom):
    x_ = (right-left)/2
    y_ = (bottom-top)/2

    w = right - left
    h = bottom - top
    aspect_ratio = w/h

    if 0.8 < aspect_ratio <= 1:
        return type1, x_, y_
    elif 0 < aspect_ratio <= 0.8:
        return type2, x_, y_
    elif 1 < aspect_ratio <= 2.5:
        return type4, x_, y_
    else:
        return type3, x_, y_
    
print(get_panel_type(0,910,0,612))




