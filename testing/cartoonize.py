# # Import necessary libraries
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# def cartoonize():
#     # Opens an image with cv2
#     img = cv2.imread('frames/final/frame007.png')

#     # Apply some Gaussian blur on the image
#     img_gb = cv2.GaussianBlur(img, (7, 7) ,0)
#     # Apply some Median blur on the image
#     img_mb = cv2.medianBlur(img_gb, 5)
#     # Apply a bilateral filer on the image
#     img_bf = cv2.bilateralFilter(img_mb, 5, 80, 80)

#     # Convert from BGR back to RGB
#     img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img_gb_RGB = cv2.cvtColor(img_gb, cv2.COLOR_BGR2RGB)
#     img_mb_RGB = cv2.cvtColor(img_mb, cv2.COLOR_BGR2RGB)
#     img_bf_RGB = cv2.cvtColor(img_bf, cv2.COLOR_BGR2RGB)

#     # Plot the image to see some differences.
#     f, axarr = plt.subplots(2, 2, figsize=(25, 25))
#     axarr[0,0].imshow(img_RGB)
#     axarr[0,0].title.set_text('Original')
#     axarr[0,1].imshow(img_gb_RGB)
#     axarr[0,1].title.set_text('Original + GaussianBlur')
#     axarr[1,0].imshow(img_mb_RGB)
#     axarr[1,0].title.set_text('Original + GaussianBlur + MedianBlur')
#     axarr[1,1].imshow(img_bf_RGB)
#     axarr[1,1].title.set_text('Original + GaussianBlur + MedianBlur + BilaterFilter')

#     # Save the figure if needed
#     plt.savefig('FilterComparisons.png')

#     # Use the laplace filter to detect edges
#     img_lp_im = cv2.Laplacian(img, cv2.CV_8U, ksize=5)
#     img_lp_gb = cv2.Laplacian(img_gb, cv2.CV_8U, ksize=5)
#     img_lp_mb = cv2.Laplacian(img_mb, cv2.CV_8U, ksize=5)
#     img_lp_al = cv2.Laplacian(img_bf, cv2.CV_8U, ksize=5)

#     # Plot the image to see some differences.
#     f, axarr = plt.subplots(2,2, figsize=(25, 25))
#     axarr[0,0].imshow(img_lp_im, cmap='gray', vmin=0, vmax=255)
#     axarr[0,0].title.set_text('Original')
#     axarr[0,1].imshow(img_lp_gb, cmap='gray', vmin=0, vmax=255)
#     axarr[0,1].title.set_text('Original + GaussianBlur')
#     axarr[1,0].imshow(img_lp_mb, cmap='gray', vmin=0, vmax=255)
#     axarr[1,0].title.set_text('Original + GaussianBlur + MedianBlur')
#     axarr[1,1].imshow(img_lp_al, cmap='gray', vmin=0, vmax=255)
#     axarr[1,1].title.set_text('Original + GaussianBlur + MedianBlur + BilaterFilter')

#     # Save the figure if needed
#     plt.savefig('LaplacianComparison.png')

#     # Convert the image to greyscale (1D)
#     img_lp_im_grey = cv2.cvtColor(img_lp_im, cv2.COLOR_BGR2GRAY)
#     img_lp_gb_grey = cv2.cvtColor(img_lp_gb, cv2.COLOR_BGR2GRAY)
#     img_lp_mb_grey = cv2.cvtColor(img_lp_mb, cv2.COLOR_BGR2GRAY)
#     img_lp_al_grey = cv2.cvtColor(img_lp_al, cv2.COLOR_BGR2GRAY)

#     # Remove some additional noise
#     blur_im = cv2.GaussianBlur(img_lp_im_grey, (5, 5), 0)
#     blur_gb = cv2.GaussianBlur(img_lp_gb_grey, (5, 5), 0)
#     blur_mb = cv2.GaussianBlur(img_lp_mb_grey, (5, 5), 0)
#     blur_al = cv2.GaussianBlur(img_lp_al_grey, (5, 5), 0)

#     # Apply a threshold (Otsu)
#     _, tresh_im = cv2.threshold(blur_im, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     _, tresh_gb = cv2.threshold(blur_gb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     _, tresh_mb = cv2.threshold(blur_mb, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     _, tresh_al = cv2.threshold(blur_al, 245, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#     # Invert the black and the white
#     inverted_original = cv2.subtract(255, tresh_im)
#     inverted_GaussianBlur = cv2.subtract(255, tresh_gb)
#     inverted_MedianBlur = cv2.subtract(255, tresh_mb)
#     inverted_Bilateral = cv2.subtract(255, tresh_al)

#     # Plot the image to see some differences.
#     f, axarr = plt.subplots(2,2, figsize=(25, 25))
#     axarr[0,0].imshow(inverted_original, cmap='gray', vmin=0, vmax=255)
#     axarr[0,0].title.set_text('Original')
#     axarr[0,1].imshow(inverted_GaussianBlur, cmap='gray', vmin=0, vmax=255)
#     axarr[0,1].title.set_text('Original + GaussianBlur')
#     axarr[1,0].imshow(inverted_MedianBlur, cmap='gray', vmin=0, vmax=255)
#     axarr[1,0].title.set_text('Original + GaussianBlur + MedianBlur')
#     axarr[1,1].imshow(inverted_Bilateral, cmap='gray', vmin=0, vmax=255)
#     axarr[1,1].title.set_text('Original + GaussianBlur + MedianBlur + BilaterFilter')

#     # Save the figure if needed
#     plt.savefig('treshingComparison.png')

#     # Reduce the colors of the original image
#     div = 64
#     img_bins = img // div * div + div // 2

#     # Reshape the image
#     img_reshaped = img.reshape((-1,3))
#     # convert to np.float32
#     img_reshaped = np.float32(img_reshaped)
#     # Set the Kmeans criteria
#     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#     # Set the amount of K (colors)
#     K = 20
#     # Apply Kmeans
#     _, label, center = cv2.kmeans(img_reshaped, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#     # Covert it back to np.int8
#     center = np.uint8(center)
#     res = center[label.flatten()]
#     # Reshape it back to an image
#     img_Kmeans = res.reshape((img.shape))

#     # Convert BGR back to RGB
#     img_Kmeans_RGB = cv2.cvtColor(img_Kmeans, cv2.COLOR_BGR2RGB)
#     img_bins_RGB = cv2.cvtColor(img_bins, cv2.COLOR_BGR2RGB)

#     # Plot the binned images to see  differences.
#     f, axarr = plt.subplots(1, 2, figsize=(25, 25))
#     axarr[0].imshow(img_Kmeans_RGB)
#     axarr[0].title.set_text('img_Kmeans')
#     axarr[1].imshow(img_bins_RGB)
#     axarr[1].title.set_text('img_bins')

#     plt.savefig('colorReduce.png')

#     # Convert the mask image back to color
#     inverted_Bilateral = cv2.cvtColor(inverted_Bilateral, cv2.COLOR_GRAY2RGB)
#     # Combine the edge image and the binned image
#     cartoon_Bilateral = cv2.bitwise_and(inverted_Bilateral, img_Kmeans)

#     # Save the image
#     cv2.imwrite('CartoonImage.png', cartoon_Bilateral)

# # cartoonize()
import math

import numpy as np
from skimage.io import imread, imsave

sample_img = imread('frames/final/frame001.png')
colors = 32
def median_cut_quantize(img, img_arr):
    # when it reaches the end, color quantize
    r_average = np.mean(img_arr[:, 0])
    g_average = np.mean(img_arr[:, 1])
    b_average = np.mean(img_arr[:, 2])

    for data in img_arr:
        sample_img[data[3]][data[4]] = [r_average, g_average, b_average]


def split_into_buckets(img, img_arr, depth):
    if len(img_arr) == 0:
        return

    if depth == 0:
        median_cut_quantize(img, img_arr)
        return

    r_range = np.max(img_arr[:, 0]) - np.min(img_arr[:, 0])
    g_range = np.max(img_arr[:, 1]) - np.min(img_arr[:, 1])
    b_range = np.max(img_arr[:, 2]) - np.min(img_arr[:, 2])

    space_with_highest_range = 0

    if g_range >= r_range and g_range >= b_range:
        space_with_highest_range = 1
    elif b_range >= r_range and b_range >= g_range:
        space_with_highest_range = 2
    elif r_range >= b_range and r_range >= g_range:
        space_with_highest_range = 0

    # sort the image pixels by color space with highest range
    # and find the median and divide the array.
    img_arr = img_arr[img_arr[:, space_with_highest_range].argsort()]
    median_index = int((len(img_arr) + 1) / 2)

    # split the array into two blocks
    split_into_buckets(img, img_arr[0:median_index], depth - 1)
    split_into_buckets(img, img_arr[median_index:], depth - 1)


flattened_img_array = []
for rindex, rows in enumerate(sample_img):
    for cindex, color in enumerate(rows):
        flattened_img_array.append([color[0], color[1], color[2], rindex, cindex])

flattened_img_array = np.array(flattened_img_array)

# start the splitting process
split_into_buckets(sample_img, flattened_img_array, colors)

# save the final image
imsave('CartoonImage.png', sample_img)