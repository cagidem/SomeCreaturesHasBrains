from Simulator import GridObj

GridSizes= [15,15]
EpochNumber= 30
FramesPerEpoch= 300
CreatureNumber= 25
geneNumber= 3
RemovedParts= [0,7,0,7] #left,right,up,down borders

if __name__ == "__main__":
    grid = GridObj()
    grid.Run(GridSizes,EpochNumber,FramesPerEpoch,CreatureNumber,geneNumber,RemovedParts)

