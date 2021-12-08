from Simulator import GridObj

GridSizes= [50,50]
EpochNumber= 100
FramesPerEpoch= 100
CreatureNumber= 100
geneNumber= 10
interNeuronNumber = 5
RemovedParts= [10,40,10,40] #left,right,up,down borders

if __name__ == "__main__":
    grid = GridObj()
    grid.Run(GridSizes,EpochNumber,FramesPerEpoch,CreatureNumber,geneNumber,interNeuronNumber,RemovedParts)

