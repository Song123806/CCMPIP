import numpy as np
import torch
import random
from sklearn.model_selection import train_test_split
from utils import standardize_features_with_train_rules

'''''''''''''''''''''''''test_data'''''''''''''''''''''''''
test_x_tensor = torch.load('../dataset/ProtT5/test_t5.pt')
test_aaindex = torch.load('../dataset/test_aaindex_std.pt ')
test_y_tensor = [1]*171 + [0]*171
