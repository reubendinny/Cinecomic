from PIL import Image
from backend.panel_layout.cam import get_coordinates

def crop_image(img_path):
    img = Image.open(img_path)
    left, top, right, bottom = get_coordinates(img_path)
    # Crop the image wrt the 4 coordinates
    box = (left, top, right, bottom)
    img2 = img.crop(box)
    
    # Save the cropped image
    # img2.save('croppedframe_cropped.jpg')
    # img2.show()
    return img2