import numpy as np

X = np.load('X_gd.npy')
y = np.load('y_gd.npy')

np.savetxt('X_gd.txt', X, delimiter=',')
np.savetxt('y_gd.txt', y, delimiter=',')