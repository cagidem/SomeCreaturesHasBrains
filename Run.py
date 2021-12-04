from Simulator import GridObj

GridSizes= [10,10]
EpochNumber= 50
FramesPerEpoch= 300
CreatureNumber= 25
geneNumber= 10
interNeuronNumber = 15
RemovedParts= [0,5,0,11] #left,right,up,down borders

if __name__ == "__main__":
    grid = GridObj()
    grid.Run(GridSizes,EpochNumber,FramesPerEpoch,CreatureNumber,geneNumber,interNeuronNumber,RemovedParts)

