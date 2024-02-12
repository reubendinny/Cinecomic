from PIL import Image
from cam import get_coordinates

img_path = 'frames/final/frame026.png'
img = Image.open(img_path)
# img.show()
left, top, right, bottom = get_coordinates(img_path)
# Crop the image wrt the 4 coordinates
box = (left, top, right, bottom)
img2 = img.crop(box)
# Save the cropped image
# img2.save('croppedframe_cropped.jpg')
img2.show()