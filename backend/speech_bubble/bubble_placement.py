from backend.utils import convert_to_css_pixel, get_panel_type, types

BUBBLE_WIDTH = 200
BUUBLE_HEIGHT = 94

def add_bubble_padding(least_roi_x, least_roi_y, crop_coord):
    left,right,top,bottom = crop_coord
    panel = get_panel_type(left, right, top, bottom)
    
    image_width = types[panel]['width']
    image_height = types[panel]['height']

    if least_roi_x == 0:
        if panel == '1' or panel == '2':
            least_roi_x += 10
        elif panel == '3':
            least_roi_x += 30
        else:
            least_roi_x += 20

    elif least_roi_x == image_width:
        least_roi_x -= BUBBLE_WIDTH + 15

    elif least_roi_x >= image_width - BUBBLE_WIDTH:
        least_roi_x -= BUBBLE_WIDTH - (image_width - least_roi_x) + 15

    if least_roi_y == 0:
        if panel == '2':
            least_roi_y += 30
        else:
            least_roi_y += 15

    elif least_roi_y == image_height:
        least_roi_y -= BUUBLE_HEIGHT + 15

    elif least_roi_y >= image_height - BUUBLE_HEIGHT:
        least_roi_y -= BUUBLE_HEIGHT - (image_height - least_roi_y) + 15
    
    return least_roi_x, least_roi_y


def get_bubble_position(crop_coord, CAM_data):
    left, right, top, bottom = crop_coord
    x_ = CAM_data['x_']
    y_ = CAM_data['y_']
    ten_map = CAM_data['ten_map']
    print(ten_map)

    new_top = int(top / y_)
    new_bottom = int(bottom / y_)
    new_left = int(left / x_)
    new_right = int(right / x_)
    print(new_top, new_bottom, new_left, new_right)

    # Initialize variables to store the minimum value and its corresponding index
    min_value = float('inf')  # Initialize min value to positive infinity
    min_point = None  # Initialize min point to None

    # Top
    found = False
    for i in range(new_left, new_right + 1):
        for j in range(new_top, new_bottom + 1):
            if (i < ten_map.shape[0] and j < ten_map.shape[1]) and ten_map[i][j] < min_value:
                min_point = (i, j)
                min_value = ten_map[i][j]

    least_roi_x = min_point[0] * x_
    least_roi_y = min_point[1] * y_

    if least_roi_x < left:
        least_roi_x = left
    elif least_roi_x > right:
        least_roi_x = right
    if least_roi_y < top:
        least_roi_y = top
    elif least_roi_y > bottom:
        least_roi_y = bottom

    least_roi_x -= left
    least_roi_y -= top
    print("Least ROI coords: ", least_roi_x, least_roi_y)
    
    least_roi_x, least_roi_y = convert_to_css_pixel(least_roi_x,least_roi_y,crop_coord)
    print("Least ROI coords after scaling: ", least_roi_x, least_roi_y)

    least_roi_x, least_roi_y = add_bubble_padding(least_roi_x, least_roi_y, crop_coord)

    return least_roi_x, least_roi_y