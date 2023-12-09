import torch
import numpy as np

googlenet = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
print(googlenet)

googlenet = torch.nn.Sequential(*(list(googlenet.children())[:-1]))
# print(googlenet)


# sample execution (requires torchvision)
from PIL import Image

from torchvision import transforms
input_image = Image.open("video/ironman.jpg")
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    googlenet.to('cuda')

with torch.no_grad():
    output = googlenet(input_batch)
# Tensor of shape 1000, with confidence scores over ImageNet's 1000 classes
print(type(output[0]))

# numpy_array = output.numpy()

# Convert the NumPy array to np.float32
# numpy_array_float32 = output.astype(np.float32)
# # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
# probabilities = torch.nn.functional.softmax(output[0], dim=0)
# print(probabilities)
numpy_array_float32_gpu = output.to('cpu', torch.float32).numpy()
print(type(numpy_array_float32_gpu))