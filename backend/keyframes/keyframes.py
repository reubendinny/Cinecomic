# Cell 1
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from backend.keyframes.model import DSN
import torch.nn as nn
import cv2
import time
import os
import srt
from backend.keyframes.extract_frames import extract_frames
from backend.utils import copy_and_rename_file, get_black_bar_coordinates, crop_image

# Cell 2
def _get_features(frames, gpu=True, batch_size=1):
    # Load pre-trained GoogLeNet model
    googlenet = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', weights='GoogLeNet_Weights.DEFAULT')

    # Remove the classification layer (last layer) to obtain features
    googlenet = torch.nn.Sequential(*(list(googlenet.children())[:-1]))

    # Set the model to evaluation mode
    googlenet.eval()

    # Initialize a list to store the features
    features = []

    # Image preprocessing pipeline
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Iterate through frames
    for frame_path in frames:
        # Load and preprocess the frame
        input_image = Image.open(frame_path)
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)  # Add batch dimension

        # Move the input and model to GPU if available
        if gpu:
            input_batch = input_batch.to('cuda')
            googlenet.to('cuda')

        # Perform feature extraction
        with torch.no_grad():
            output = googlenet(input_batch)

        # Append the features to the list
        features.append(output.squeeze().cpu().numpy())

    # Convert the list of features to a NumPy array
    features = np.array(features)

    return features.astype(np.float32)

# Cell 3
def _get_probs(features, gpu=True, mode=0):
    # model_cache_key = "keyframes_rl_model_cache_" + str(mode)
    if mode == 1:
        model_path = "backend/keyframes/pretrained_model/model_1.pth.tar"
    else:
        model_path = "backend/keyframes/pretrained_model/model_0.pth.tar"
    model = DSN(in_dim=1024, hid_dim=256, num_layers=1, cell="lstm")
    if gpu:
        checkpoint = torch.load(model_path)
    else:
        checkpoint = torch.load(model_path, map_location='cpu')
    model.load_state_dict(checkpoint)
    if gpu:
        model = nn.DataParallel(model).cuda()
    model.eval()

    seq = torch.from_numpy(features).unsqueeze(0)
    if gpu: seq = seq.cuda()
    probs = model(seq)
    probs = probs.data.cpu().squeeze().numpy()
    return probs


   
def generate_keyframes(video):
    data=""
    with open("test1.srt") as f:
        data = f.read()

    subs = srt.parse(data)
    torch.cuda.empty_cache()

    for sub in subs:
        frames = []
        if not os.path.exists(f"frames/sub{sub.index}"):
            os.makedirs(f"frames/sub{sub.index}")
        frames = extract_frames(video,os.path.join("frames",f"sub{sub.index}"),sub.start.total_seconds(),sub.end.total_seconds(),3)
        features = _get_features(frames, gpu=False)
        highlight_scores = _get_probs(features, gpu=False)

        try:
            highlight_scores = list(highlight_scores)    
            sorted_indices = [i[0] for i in sorted(enumerate(highlight_scores), key=lambda x: x[1])]
            print(f"The indices of the list in the increasing order of value are {sorted_indices}.")
            selected_keyframe = sorted_indices[-1]
            frames[selected_keyframe]
            copy_and_rename_file(frames[selected_keyframe], os.path.join("frames","final"), f"frame{sub.index:03}.png")
        
        except(TypeError):
            copy_and_rename_file(frames[0], os.path.join("frames","final"), f"frame{sub.index:03}.png")
    

def black_bar_crop():
    ref_img_path = "frames/final/frame001.png"
    x, y, w, h = get_black_bar_coordinates(ref_img_path)
    
    # Loop through each keyframe
    folder_dir = "frames/final"
    for image in os.listdir(folder_dir): 
        img_path = os.path.join("frames",'final',image)
        image = cv2.imread(img_path)
        
        # Crop the image
        crop = image[y:y+h, x:x+w]

        # Save the cropped image
        cv2.imwrite(img_path, crop)
    return x,y,w,h