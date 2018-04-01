# Bomberman

This is a simulation of Bomberman using the Reinforcement Learning technique 'Q-Learning'.

#### Environment Description:
The dimension of the maze is 10 x 10.Thre are three types of cells in the maze .They are:
-free cells, that the bomberman can move to 
-obstacles,  that the bomberman can clear by placing a bomb in the viscinity of the obstacle
-walls, that the bomberman cannot destroy  

The agent(bomberman) is be encouraged to win the game by adherering to the following rewarding scheme:


* Movement to an adjacent free cell which has been visited already costs the bomberman -0.04 points.
This discourages the bomberman from wandering and visiting cells that have been visited already.
* Each movement to an unexplored cell is rewarded by assigning 0.04 points to the agent.
* An attempt to move toward the walls/obstacles is penal- ized (-0.75).
* An attempt to make a move to go beyond the maze boundry is also heavily penalize (-0.75)
* Placing a bomb next to the indestructible wall is penalized. (-0.8)
* If no obstacles are destroyed after a bomb is placed, then bomberman is penalized. (-0.8). This prevents the agent from wasting bombs.
* The game ends once the total reward of the agent is below the negative threshold .When the reward falls below the threshold it is concluded that the bomberman has made too many errors and a new game is started.
* Maximal point 1 is rewarded when bomberman finds the gate.

##### Acknowledgements:
The idea is based on the the article *"Deep Reinforcement Learning for Maze Solving"* http://www.samyzaf.com/ML/rl/qmaze.html
