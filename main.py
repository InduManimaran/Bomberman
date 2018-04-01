from __future__ import print_function

from buildModel import *
from qtrain import *
from QmazeParameters import *


if __name__ == '__main__':
	
	global maze
	#qmaze = Qmaze(maze)

	model = build_model(maze)

	qtrain(model,maze)

