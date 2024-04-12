# import torch
# import pickle

# exple = {'some_number': 1, 'some_tensor': torch.tensor([[1., 2., 3.]])}

# file = open('my_tensor.pkl', 'wb')
# pickle.dump(exple, file)
# file.close()

#read_pickle.py
import pickle

def read_pickle(filepath):
  file = open(filepath, 'rb')
  content = pickle.load(file)
  file.close()
  return content

content = read_pickle('my_tensor.pkl')
print(content['some_tensor'][0][1])