# from PIL import Image
# import imagehash
# import cv2

# def similar_to_keyframe(keyframe_path, frame):
#     # frame_color_coverted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # frame_pil = Image.fromarray(frame_color_coverted)       # Convert to PIL

#     hash0 = imagehash.average_hash(Image.open(frame)) 
#     hash1 = imagehash.average_hash(Image.open(keyframe_path)) 
#     cutoff = 5  # maximum bits that could be different between the hashes. 

#     print(hash0 - hash1)
#     if hash0 - hash1 < cutoff:
#       return True
#     else:
#       return False
    
# print(similar_to_keyframe('frames/final/frame005.png', 'frames/sub5/frame_2.png'))


from skimage.metrics import structural_similarity as compare_ssim

import cv2

# Load the images
original = cv2.imread('frames/final/frame005.png')
cropped = cv2.imread('frames/sub5/frame_2.png')

# Convert the images to grayscale
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cropped_gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
ssim = compare_ssim(original_gray, cropped_gray)

print("SSIM: ", ssim)
