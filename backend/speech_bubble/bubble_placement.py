def get_bubble_position(crop_coord, CAM_data):
    left, right, top, bottom = crop_coord
    print("Initial Crop Coords:", crop_coord)
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

    least_roi_x -= left
    least_roi_y -= top
    print("Least ROI coords: ", least_roi_x, least_roi_y)
    return least_roi_x, least_roi_y