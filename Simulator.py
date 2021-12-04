import numpy as np
import random
import time
from randomCreature import geneCreator
from brain import *

class GridObj:
    def __init__(self,y=0,x=0,grid=None,creatures={},lastMove=None,geneNumber = None):
        self.y = y
        self.x = x
        self.grid = grid
        self.creatures = creatures
        self.lastMove = lastMove
        self.geneNumber = geneNumber

    def creategrid(self):
        self.grid = np.zeros([self.y,self.x])
        return

    def isEmpty(self,loc):
        if self.grid[loc[0],loc[1]] == 0:
            return True
        else:
            return False

    def RandomLoc(self, n=1):
        y = self.y
        x = self.x
        locs = []
        while n > 0:
            loc = [random.randint(0,y-1),random.randint(0,x-1)]
            if self.isEmpty(loc) == True and loc not in locs:
                locs.append([loc[0],loc[1]])
                n-=1
            else:
                continue
        if len(locs) == 1:
            return locs[0]
        else:
            return locs

    def RandomCreate(self,n = 1,start = 0):
        locs = self.RandomLoc(n)
        if n == 1:
            genes = geneCreator(self.geneNumber)
            genes.append(0)
            self.grid[locs[0]][locs[1]] = n+start
            self.creatures[n] = [locs,[genes]]
        else:
            a = start + 1
            for i in locs:
                genes = geneCreator(self.geneNumber)
                genes.append(0)
                self.grid[i[0]][i[1]] = a
                self.creatures[a+start] = [i,[genes]]
                a += 1
        return

    def borders(self, loc):
        results = [False,False,False,False] #[right,left,up,down]
        
        if loc[1]+1 < self.x:
            pass
        else:
            results[0] = True

        if loc[1]-1 >= 0:
            pass
        else:
            results[1] = True

        if loc[0]-1 >= 0:
            pass
        else:
            results[2] = True

        if loc[0]+1 < self.y:
            pass
        else:
            results[3] = True
        
        return results
    
    def surroundings(self, loc):
        RightBorder, LeftBorder, UpBorder, DownBorder = self.borders(loc)
        results = np.zeros([3,3])

        if RightBorder == True:
            for i in range(3):
                results[i][2] = -1
        

        if LeftBorder == True:
            for i in range(3):
                results[i][0] = -1
        

        if UpBorder == True:
            results[0] = [-1,-1,-1]
        
        
        if DownBorder == True:
            results[2] = [-1,-1,-1]
        
        for i in range(-1,2):
            for j in range(-1,2):
                if results[i+1][j+1] != -1:
                    results[i+1][j+1] = self.grid[loc[0]+i][loc[1]+j]

        return results

    
    def moveRight(self,loc):
        if loc[1]+1 < self.x:
            nextLoc = [loc[0],loc[1]+1]
            temp = self.grid[loc[0]][loc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return
        if self.isEmpty(nextLoc) == True:
            self.grid[loc[0]][loc[1]] = 0
            self.grid[nextLoc[0]][nextLoc[1]] = temp
            self.lastMove = [nextLoc[0],nextLoc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return

    def moveLeft(self,loc):
        if loc[1]-1 >= 0:
            nextLoc = [loc[0],loc[1]-1]
            temp = self.grid[loc[0]][loc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return
        if self.isEmpty(nextLoc) == True:
            self.grid[loc[0]][loc[1]] = 0
            self.grid[nextLoc[0]][nextLoc[1]] = temp
            self.lastMove = [nextLoc[0],nextLoc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return

    def moveUp(self,loc):
        if loc[0]-1 >= 0:
            nextLoc = [loc[0]-1,loc[1]]
            temp = self.grid[loc[0]][loc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return
        if self.isEmpty(nextLoc) == True:
            self.grid[loc[0]][loc[1]] = 0
            self.grid[nextLoc[0]][nextLoc[1]] = temp
            self.lastMove = [nextLoc[0],nextLoc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return

    def moveDown(self,loc):
        if loc[0]+1 < self.y:
            nextLoc = [loc[0]+1,loc[1]]
            temp = self.grid[loc[0]][loc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return
        if self.isEmpty(nextLoc) == True:
            self.grid[loc[0]][loc[1]] = 0
            self.grid[nextLoc[0]][nextLoc[1]] = temp
            self.lastMove = [nextLoc[0],nextLoc[1]]
        else:
            self.lastMove = [loc[0],loc[1]]
            return
    
    def MoveRandom(self,loc):
        surr = self.surroundings(loc)
        i = 0
        while i < 20:
            nextLocy = random.randint(-1,1)
            nextLocx = random.randint(-1,1)
            temp = self.grid[loc[0]][loc[1]]
            
            if surr[nextLocy+1][nextLocx+1] == 0:
                self.grid[loc[0]][loc[1]] = 0
                self.grid[loc[0]+nextLocy][loc[1]+nextLocx] = temp
                self.lastMove = [loc[0]+nextLocy,loc[1]+nextLocx]
                i = 20
            else:
                i+=1 
                continue
        else:
            self.lastMove = [loc[0],loc[1]]
        return

    def FrameUpdate(self):
        for i in self.creatures:    
            location = self.creatures[i][0]
            distance = [(self.y-location[0])/self.y,(self.x-location[1])/self.x]
            genetic = self.creatures[i][1][0][:self.geneNumber]
            #print(i)
            points = self.creatures[i][1][0][self.geneNumber:]
            #print(points)
            surr = self.surroundings(location)
            interNeuron = 3
            creatureMove = move(genetic, distance, surr, points, interNeuron)
            #print(location)
            if creatureMove == "R":
                self.moveRight([location[0],location[1]])
                self.creatures[i][0] = self.lastMove
                #print(f"Creature {i} to R")
            elif creatureMove == "L":
                self.moveLeft([location[0],location[1]])
                self.creatures[i][0] = self.lastMove
                #print(f"Creature {i} to L")
            elif creatureMove == "U":
                self.moveUp([location[0],location[1]])
                self.creatures[i][0] = self.lastMove
                #print(f"Creature {i} to U")
            elif creatureMove == "D":
                self.moveDown([location[0],location[1]])
                self.creatures[i][0] = self.lastMove
                #print(f"Creature {i} to D")
            elif creatureMove == "Rand":
                self.MoveRandom([location[0],location[1]])
                self.creatures[i][0] = self.lastMove
                #print(f"Creature {i} Random Move")
            next
        return

    def Remove(self,LeftRemoveBorder,RightRemoveBorder,UpRemoveBorder,DownRemoveBorder):
        deleted = []
        for i in self.creatures:
            if self.creatures[i][0][0] < DownRemoveBorder and self.creatures[i][0][0] >= UpRemoveBorder and self.creatures[i][0][1] >= LeftRemoveBorder and self.creatures[i][0][1] < RightRemoveBorder:
                loc = self.creatures[i][0]
                self.grid[loc[0]][loc[1]] = 0
                deleted.append(i)
        for j in deleted:
            DelLoc = self.creatures[j][0]
            self.creatures.pop(j)
            self.grid[DelLoc[0]][DelLoc[1]] = 0
        return

    def CreateNew(self,CreatureNumber):
        if len(self.creatures) != 0:
            MaxNum = max(self.creatures)
        else:
            MaxNum = 0
        if len(self.creatures) < CreatureNumber:
            self.RandomCreate(n=CreatureNumber - len(self.creatures),start=MaxNum)
        return

    def CreateNew2(self,CreatureNumber):
        for i in range(1,CreatureNumber+1):
            if i not in self.creatures:
                loc = self.RandomLoc()
                genes = geneCreator(self.geneNumber)
                genes.append(0)
                self.creatures[i] = [loc,[genes]]
        return

    def CreateNew3(self, CreatureNumber):
        tempGenetic = self.creatures[random.choice(list(self.creatures))][1]
        for i in range(1,CreatureNumber+1):
            if i not in self.creatures:
                loc = self.RandomLoc()
                self.creatures[i] = [loc,tempGenetic]
            else:
                tempGenetic = self.creatures[i][1]
        return
    
    def LocationRes(self,):
        locs = self.RandomLoc(len(self.creatures))
        for i in self.creatures:
            loc = random.choice(locs)
            locs.remove(loc)
            gene = self.creatures[i][1]
            self.creatures[i] = [loc,gene]

    def GridRes(self):
        self.creategrid()
        for i in self.creatures:
            loc = self.creatures[i][0]
            self.grid[loc[0]][loc[1]]=i
        return

    def Run(self, GridSizes=[0,0], EpochNumber=0, FramesPerEpoch=0, CreatureNumber=0,geneNumber = 0, RemovedParts=[0,0,0,0]):
        self.y = GridSizes[0]
        self.x = GridSizes[1]
        self.geneNumber = geneNumber
        self.creategrid()
        self.RandomCreate(CreatureNumber)
        print("Starting...")
        print(self.grid)
        for epoch in range(EpochNumber):
            asd = time.time()
            for __ in range(FramesPerEpoch):
                self.FrameUpdate()
                #print(self.grid)
            print(time.time()-asd)
            self.Remove(RemovedParts[0],RemovedParts[1],RemovedParts[2],RemovedParts[3])
            if len(self.creatures) == 0:
                print("No creatures left. Terminated Early")
                return
            self.CreateNew3(CreatureNumber)
            self.LocationRes()
            self.GridRes()
            print(f"Epoch = {epoch+1}")
            print(self.grid)
        return
