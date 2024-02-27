# import cv2
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# sample_images = "../frames/final/frame006.png"

# image = cv2.imread(sample_images)
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(image_gray, 1, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# biggest = np.array([])
# max_area = 0
# for cntrs in contours:
#     area = cv2.contourArea(cntrs)
#     peri = cv2.arcLength(cntrs, True)
#     approx = cv2.approxPolyDP(cntrs, 0.02 * peri, True)
#     if area > max_area and len(approx) == 4:
#         biggest = approx
#         max_area = area

# cnt = biggest
# print("cnt: ", cnt, "cnt[0][0][0]: ", cnt[0][0][0])
# # if cnt[0][0][0] == 0:
# x, y, w, h = cv2.boundingRect(cnt)
# crop = image[y:y+h, x:x+w]

# # Save the cropped image
# cv2.imwrite("cropped/crop6.png", crop)

###########################################################

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image_path = "../frames/final/frame012.png"
image2_path = "../frames/final/frame013.png"

try:
    # Read the image
    image = cv2.imread(image_path)
    image2 = cv2.imread(image2_path)

    # Convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding
    _, thresh = cv2.threshold(image_gray, 1, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour with four corners
    largest_contour = np.array([])
    max_area = 0
    for cntrs in contours:
        area = cv2.contourArea(cntrs)
        print("area1=", area, " maxarea1 = ", max_area)
        peri = cv2.arcLength(cntrs, True)
        approx = cv2.approxPolyDP(cntrs, 0.02 * peri, True)
        # if area > max_area and len(approx) == 4:
        if area > max_area:
            largest_contour = approx
            max_area = area
        print("area2", area, " maxarea2 = ", max_area)

    # Extract bounding box
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the image
    cropped_image = image[y:y+h, x:x+w]
    # Save the cropped image
    cv2.imwrite("out012.png", cropped_image)

    # Crop the image
    cropped_image = image2[y:y+h, x:x+w]
    # Save the cropped image
    cv2.imwrite("out013.png", cropped_image)

except Exception as e:
    print(f"Error: {e}")