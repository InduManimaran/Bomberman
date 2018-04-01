# The CNN 
# It is a sequential model with a two dense layers with Prelu activation functions
#The optimizer used is adam

from keras.models import Sequential
from keras.layers import PReLU, Dense
from QmazeParameters import *
def build_model(maze, lr=0.001):
    global num_actions
    model = Sequential()
    model.add(Dense(maze.size, input_shape=(maze.size,)))
    model.add(PReLU())
    model.add(Dense(maze.size))
    model.add(PReLU())
    model.add(Dense(num_actions))
    model.compile(optimizer='adam', loss='mse')
    return model
