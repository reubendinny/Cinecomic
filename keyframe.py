import torch
from torchvision import transforms
from PIL import Image
import numpy as np

def _get_features(frames, gpu=True, batch_size=1):
    # Load pre-trained GoogLeNet model
    googlenet = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
    
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


frames = ["video/ironman.jpg"]
print(_get_features(frames))
