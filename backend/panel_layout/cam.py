import matplotlib.pyplot as plt
from torchcam.utils import overlay_mask
import numpy as np
from torch import tensor
import operator


from torchvision.models import resnet18
model = resnet18(pretrained=True).eval()

# Set your CAM extractor
from torchcam.methods import SmoothGradCAMpp
cam_extractor = SmoothGradCAMpp(model)

from torchvision.io.image import read_image
from torchvision.transforms.functional import normalize, resize, to_pil_image
from torchvision.models import resnet18
from torchcam.methods import SmoothGradCAMpp
import pickle

model = resnet18(pretrained=True).eval()

CAM_data = []

def dump_CAM_data():
    # Dumping CAM_data
    with open('CAM_data.pkl', 'wb') as f:
        pickle.dump(CAM_data, f)

def get_coordinates(img_path):
    # Get your input
    img = read_image(img_path)
    # Preprocess it for your chosen model
    input_tensor = normalize(resize(img, (224, 224)) / 255., [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

    with SmoothGradCAMpp(model) as cam_extractor:
      # Preprocess your data and feed it to the model
      out = model(input_tensor.unsqueeze(0))
      # Retrieve the CAM by passing the class index and the model output
      activation_map = cam_extractor(out.squeeze(0).argmax().item(), out)

    cam_map = activation_map[0][0]
    arr = np.array(cam_map.cpu())
    ten_map = tensor(arr)
    print("TENMAP",arr)
    cms = cam_map.shape[0]

    x_ = img.shape[2] // cms
    y_ = img.shape[1] // cms

    CAM_data.append({'x_': x_, 'y_': y_, 'ten_map': arr})

    top,bottom,left,right = -1,-1,-1,-1
    threshold = 0.2

    # Top
    found = False
    for i in range(0, ten_map.shape[0]):
        for j in range(0,ten_map.shape[1]):
          if ten_map[i][j] >= threshold:
            top = i
            found = True
            break
        if found:
          break
        
    #Bottom
    found = False
    for i in range(ten_map.shape[0]-1, -1, -1):
        for j in range(0,ten_map.shape[1]):
          if ten_map[i][j] >= threshold:
            bottom = i
            found = True
            break
        if found:
          break
        
    #Left
    found = False
    for j in range(0, ten_map.shape[1]):
        for i in range(0,ten_map.shape[0]):
          if ten_map[i][j] >= threshold:
            left = j
            found = True
            break
        if found:
          break
        
    #Right
    found = False
    for j in range(ten_map.shape[1]-1, -1, -1):
        for i in range(0,ten_map.shape[0]):
          if ten_map[i][j] >= threshold:
            right = j
            found = True
            break
        if found:
          break
        
    top = top * y_
    bottom = bottom * y_
    left = left * x_
    right = right * x_
    left,right,top,bottom

    return left, right, top, bottom