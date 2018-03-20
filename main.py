from __future__ import print_function


import numpy as np
import time
from buildModel import *
from qtrain import *



if __name__ == '__main__':

	#qmaze = Qmaze(maze)

	model = build_model(maze)

	qtrain(model,maze)

