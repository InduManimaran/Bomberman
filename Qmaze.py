import numpy as np
from matplotlib import colors
import QmazeParameters
import os, sys, time, datetime, json, random


class Qmaze(object):
    def __init__(self, maze, b_man=(0,0)):
        self._maze = np.array(maze)
        nrows, ncols = self._maze.shape
        self.target = (1,9)             # target cell where the "gate" is located
        self.tr=1                       #target row
        self.tc=9                       #target column
        self.free_cells = [(r,c) for r in range(nrows) for c in range(ncols) if self._maze[r,c] == 1.0]
        self.reset(b_man)
        self.target_status='hidden'
        self.maze[0,0]=-0.5440211


    def reset(self, b_man):
        self.b_man = b_man
        self.maze = np.copy(self._maze)
        nrows, ncols = self.maze.shape
        row, col = b_man[0],b_man[1]
        self.maze[row, col] = bm_mark
        self.state = (row, col, 'start')
        self.min_reward = -0.5 * self.maze.size
        self.total_reward = 0
        self.visited = set()


    # The cell where Bomberman is placed initially
    def setEntryGate(self):
        self.maze[0,0]=-0.5440211


    def update_state(self, action):
        self.setEntryGate()
        nrows, ncols = self.maze.shape
        nrow, ncol, nmode = bm_row, bm_col, mode = self.state

        if self.maze[bm_row, bm_col] > 0.0:
            self.visited.add((bm_row, bm_col))  # mark visited cell


        # get a list of valid moves from the current cell
        valid_actions = self.valid_actions()      
           

         #if there are no valid moves then bomberman is blocked.. restat game        
        if not valid_actions:
            nmode = 'blocked'  
        elif action in valid_actions:
            nmode = 'valid'
            if action == LEFT:
                ncol -= 1
            elif action == UP:
                nrow -= 1
            if action == RIGHT:
                ncol += 1
            elif action == DOWN:
                nrow += 1
            if action == BOMB:
                nmode=self.blowBomb(nrow,ncol)            # can create a new nmode = 'bomb' and set a different reward value
        else:                  # invalid action, no change in bombermans' position
            nmode = 'invalid'

        # new state
        self.state = (nrow, ncol, nmode)


    #   Clear obstacles if present
    def blowBomb(self,row,col):
        nrows, ncols = self.maze.shape

        ret='invalid'
        possible_locs= [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

        for x in possible_locs:
            try:
                if x[0]==-1 || x[1]==-1:
                    raise Exception
                if self.maze[x[0],x[1]]==0.5:
                    ret='valid'
                    self.maze[x[0],x[1]]=1
            except Exception :
                pass

        if (self.tr,self.tc) in possible_locs:
            self.target_status='discovered'
            self.maze[self.tr,self.tc]=-0.5440211

        return ret


    def get_reward(self):
        row, col, mode = self.state
        nrows, ncols = self.maze.shape
        if row == self.tr and col == self.tc:
            return 1.0
        if mode == 'blocked':
            return self.min_reward - 1
        if (row, col) in self.visited:
            return -0.25
        if mode == 'invalid':
            return -0.75
        if mode == 'valid':
            return 0.04

    def act(self, action):
        self.update_state(action)
        reward = self.get_reward()
        self.total_reward += reward
        status = self.game_status()
        envstate = self.observe()
        return envstate, reward, status

    def observe(self):
        canvas = self.draw_env()
        envstate = canvas.reshape((1, -1))
        return envstate

    def draw_env(self):
        canvas = np.copy(self.maze)
        nrows, ncols = self.maze.shape
        # clear all visual marks
        for r in range(nrows):
            for c in range(ncols):
                if canvas[r,c] > 0.0:
                    canvas[r,c] = 1.0
        
        # mark Bombermans's position
        row, col, valid = self.state
        canvas[row, col] = bm_mark
        return canvas

    def game_status(self):
        if self.total_reward < self.min_reward:
            return 'lose'
        row, col, mode = self.state
        nrows, ncols = self.maze.shape
        if row == self.tr and col == self.tc:
            return 'win'

        return 'not_over'

    def valid_actions(self, cell=None):
        if cell is None:
            row, col, mode = self.state
        else:
            row, col = cell

        #[left, up ,right,down,bomb]
        actions=[LEFT,RIGHT,UP,DOWN,BOMB]
        

        nrows, ncols = self.maze.shape
        
        if row == 0:
            actions.remove(UP)
        elif row == nrows-1:
            actions.remove(DOWN)

        if col == 0:
            actions.remove(LEFT)
        elif col == ncols-1:
            actions.remove(RIGHT)
        
#Removing invalid moves when Bomberman is next to an indestructible wall:
        try:
            if row>0 and self.maze[row-1,col] == 0.0:
                actions.remove(UP)
            if row<nrows-1 and self.maze[row+1,col] == 0.0:
                actions.remove(DOWN)

            if col>0 and self.maze[row,col-1] == 0.0:
                actions.remove(LEFT)

            if col<ncols-1 and self.maze[row,col+1]==0:
                actions.remove(RIGHT)

        except Exception:
            pass


# Remove invalid moves when Bomberman encounters a destructible wall
        try:

            if  self.maze[row-1,col] == 0.5:
                actions.remove(UP)
            if self.maze[row+1,col] == 0.5:
                actions.remove(DOWN)

            if self.maze[row,col-1] == 0.5:
                actions.remove(LEFT)

            if self.maze[row,col+1] == 0.5:
                actions.remove(RIGHT)

        except Exception:
            pass


        # Determining if placing a bomb is a valid move
        possible_locs= [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

        bomb=False

        for x in possible_locs:
            try:
                if x[0]==-1 || x[1]==-1:
                    raise Exception
                if self.maze[x[0],x[1]]==0.5 or self.maze[x[0],x[1]]== 0:
                    bomb=True
                    break
            except Exception :
                pass

        if bomb==False:
            actions.remove(BOMB)

        return actions



