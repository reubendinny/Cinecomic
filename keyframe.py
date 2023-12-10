import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from model import DSN
import torch.nn as nn
import cv2
import time



import cv2
import time
import os

# Function to extract frames at a specified frame rate and append paths to a list
def extract_frames(video_path, output_folder, frame_rate=2):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    frame_width = int(cap.get(3))  # Get the width of the frames
    frame_height = int(cap.get(4))  # Get the height of the frames
    
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed
    output_path = os.path.join(output_folder, "output_video.mp4")
    out = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))
    
    start_time = time.time()
    frame_count = 0
    frames = []  # List to store frame paths
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1.0 / frame_rate:
            out.write(frame)
            frame_count += 1
            start_time = time.time()

            # Save the frame as an image file
            frame_filename = f"frame_{frame_count:04d}.png"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)
            frames.append(frame_path)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    print(f"Frames extracted: {frame_count}")
    print(f"Frames per second: {frame_rate}")
    print(f"Output video saved to: {output_path}")

    return frames

# Example usage
video_path = "./video/IronMan.mp4"
output_folder = "./frames"
frames = extract_frames(video_path, output_folder, frame_rate=2)

# Now 'extracted_frame_paths' contains a list of file paths for the extracted frames
print("Extracted frame paths:", frames)




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




def _get_probs(features, gpu=True, mode=0):
        model_cache_key = "keyframes_rl_model_cache_" + str(mode)
        # model = cache.get(model_cache_key)  # get model from cache

        # if model is None:
        if mode == 1:
            model_path = "pretrained_model/model_1.pth.tar"
        else:
            model_path = "pretrained_model/model_0.pth.tar"
        model = DSN(in_dim=1024, hid_dim=256, num_layers=1, cell="lstm")
        if gpu:
            checkpoint = torch.load(model_path)
        else:
            checkpoint = torch.load(model_path, map_location='cpu')
        model.load_state_dict(checkpoint)
        if gpu:
            model = nn.DataParallel(model).cuda()
        model.eval()
        # cache.set(model_cache_key, model, None)

        seq = torch.from_numpy(features).unsqueeze(0)
        if gpu: seq = seq.cuda()
        probs = model(seq)
        probs = probs.data.cpu().squeeze().numpy()
        return probs


# print(_get_features(frames))
#print(_get_probs(_get_features(frames)))

features = _get_features(frames)
print(features.shape)
print(features[0].shape)
print(_get_probs(features).shape)
