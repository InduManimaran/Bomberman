"""
	1	-	Free cell
	0	-	Indestructible wall
	0.5	-	Desctructible wall

"""

maze = np.array([
    [ 1.,  0.,  1.,  1.,  1.,  1.,  1.,  0.5, 0.5,  0.5],
    [ 1.,  1.,  1,  1.,  1.,  0.,  1.,  1.,  0.5,  0.5],
    [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
    [ 0.,  0.,  1.,  0.,  0.,  1.,  0.,  1.,  1.,  1.],
    [ 1.,  1.,  0.,  1.,  0.,  1.,  0.,  0.,  0.,  1.],
    [ 1.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.],
    [ 1.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  0.,  1.],
    [ 1,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.]
])



cmap = colors.ListedColormap(['green','red','black','yellow'])
#cmap = colors.ListedColormap(['y','r','b','w','g'])


visited_mark = 0.8       # Cells visited by the bomberman will be painted by gray 0.8
bm_mark = 0.9287952     # The current cell that bomberman occupies


'''
Assign numeric values to to bombermans valid actions for easy of reading the program
'''
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
BOMB =4


# Actions dictionary - The valid actions that bomberman can perform
actions_dict = {
    LEFT: 'left',
    UP: 'up',
    RIGHT: 'right',
    DOWN: 'down',
    BOMB:'bomb'

}


num_actions = len(actions_dict)

epsilon = 0.4







