# Bomberman

This is a simulation of Bomberman using Q-Learning.

The agent(bomberman) is be encouraged to win the game by a adherering to the following rewarding scheme:

* Movement t oadjacent cell which has been visited already costs the bomberman -0.04 points.
This discourages the bomberman from wandering and visiting cells that have been visited already.
* Each movement to an unexplored cell is rewarded by assigning 0.04 points to the agent.
* An attempt to move toward the destructible/indestructible wall is penal- ized (-0.75).
* An attempt to make a move that would lead beyong the maze boundry is also heavily penalize (-0.75)
* Placing a bomb next to the indestructible wall is penalized. (-0.8)
* If no indestructible walls are destroyed after a bomb is placed then , bomberman is penalized. (-0.8). This prevents the agents from wasting bombs.
* The game ends once the total reward of the agent is below the negative threshold .Under the threshold i.e. the bomberman has made too many errors and a new game is started.
* Maximal point 1. Is rewarded when bomberman finds the gate.

##### Acknowledgements:
The idea is based on the the article *"Deep Reinforcement Learning for Maze Solving"* http://www.samyzaf.com/ML/rl/qmaze.html
