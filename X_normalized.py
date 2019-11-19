import numpy as np

X = np.random.random((5,5))

m = X.mean()
std = X.std()

Z = (X - m) / std