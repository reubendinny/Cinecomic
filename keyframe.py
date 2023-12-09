import torch
googlenet = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
print(googlenet)

googlenet = torch.nn.Sequential(*(list(googlenet.children())[:-1]))
print(googlenet)


