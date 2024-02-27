# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def cartoonize(img_path):
    # Opens an image with cv2
    img = cv2.imread(img_path)

    # Apply some Gaussian blur on the image
    img_gb = cv2.GaussianBlur(img, (7, 7) ,0)
    # Apply some Median blur on the image
    img_mb = cv2.medianBlur(img_gb, 5)
    # Apply a bilateral filer on the image
    img_bf = cv2.bilateralFilter(img_mb, 5, 80, 80)


    # Use the laplace filter to detect edges
    img_lp_al = cv2.Laplacian(img_bf, cv2.CV_8U, ksize=5)


    # Convert the image to greyscale (1D)
    img_lp_al_grey = cv2.cvtColor(img_lp_al, cv2.COLOR_BGR2GRAY)

    # Remove some additional noise
    blur_al = cv2.GaussianBlur(img_lp_al_grey, (5, 5), 0)

    # Apply a threshold (Otsu)
    _, tresh_al = cv2.threshold(blur_al, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Invert the black and the white
    inverted_Bilateral = cv2.subtract(255, tresh_al)

    # Reduce the colors of the original image
    # div = 64
    # img_bins = img // div * div + div // 2

    # Reshape the image
    img_reshaped = img.reshape((-1,3))
    # convert to np.float32
    img_reshaped = np.float32(img_reshaped)
    # Set the Kmeans criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # Set the amount of K (colors)
    K = 16
    # Apply Kmeans
    _, label, center = cv2.kmeans(img_reshaped, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Covert it back to np.int8
    center = np.uint8(center)
    res = center[label.flatten()]
    # Reshape it back to an image
    img_Kmeans = res.reshape((img.shape))

    # Convert the mask image back to color
    inverted_Bilateral = cv2.cvtColor(inverted_Bilateral, cv2.COLOR_GRAY2RGB)
    # Combine the edge image and the binned image
    cartoon_Bilateral = cv2.bitwise_and(inverted_Bilateral, img_Kmeans)

    # Save the image
    cv2.imwrite(img_path, cartoon_Bilateral)

# cartoonize()
    
def style_frames():
    for image in os.listdir("frames/final"):
        frame_path = os.path.join("frames",'final',image)
        cartoonize(frame_path)