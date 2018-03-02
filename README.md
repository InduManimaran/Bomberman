This project borrows ideas from Samy Zafrany post on Deep Reinforcement Learning for Maze Solving.(http://www.samyzaf.com/ML/rl/qmaze.html).


Environment Description:
	The environment is a n x n maze with three types of cells.
	1- clear 
	2- destructible wall
	3- indestructible wall 

	The cells with destructible walls can be converted to clear cells by placing bombs in their proximity.The objective of the game is for the agent (bomberman) to find the exit .The exit gate might be in one of the clear cells or it could be masked by one of the destructible walls.There are two adversaries in the environment. The layout of the environment is the same for all trials. There is no time delay for the detonation of the bomb.

Possible moves by Agent:
	The valid moves of the agent are 
1-up
2-down
3-left
4-right
5-detonate bomb


Rewards:

 Each movement to adjacent cell costs the bomberman -0.04 points.This discourages the bomberman from wandering and visiting cells that have been visited already.
 Maximal point 1. Is rewarded when bomberman finds the gate.
 An attempt to move toward the destructible/indestructible wall is penalized (-0.75)
 Placing  a bomb next to the indestructible wall is penalized. (-0.8)
 If no indestructible walls are destroyed after a bomb is placed then , bomberman is penalized. (-0.8). This prevents the agents from wasting bombs.
The game ends once the total reward of the agent is below the negative threshold .Under the threshold i.e. the bomberman has made too many errors and a new game is started.	

Other Assumptions:
	
	The bomb can be detonated only in a clear cell. The range of explosion is one cell in all directions (Up, down, left, right).It is assumed that the bomberman is immune to explosives . This makes moves to get out of the range of explosion redundant.Also, assume that the bomberman has an unlimited supply of explosives.


	The problem is based on Maze Solving described on the blog http://www.samyzaf.com/ML/rl/qmaze.html 


