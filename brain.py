import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def hexTobin(gene):
    num = bin(int(gene,16))[2:]
    if len(num)<32:
        num = ("0"*(32-len(num)))+num
    return num

def move(genetic, dist, surroundings, points,interNumber):

    surr1,surr2,surr3 = surroundings
    inputNeurons = [surr1[0],surr1[1],surr1[2],surr2[0],surr2[2],surr3[0],surr3[1],surr3[2],dist[0],dist[1],points[0]]
    interNeurons = {f"node{i}": 0 for i in range(interNumber)}
    outputNeurons = ["R","L","U","D","Rand"]
    outputData = [0,0,0,0,0]
        
    for i in genetic:
        gene = hexTobin(i)
        start = gene[0]
        startNeuron = int(gene[1:8],2)
        end = gene[8]
        endNeuron = int(gene[9:16],2)
        weight = int(gene[17:],2)/(2**13)
        #print(start)
        #print(gene)
        if start == str(0):
            sens = inputNeurons[startNeuron%len(inputNeurons)]
        else: 
            temp = startNeuron%len(interNeurons)
            sens = interNeurons[f"node{temp}"]
        #print(sens)
        try:
            sens = np.tanh(sens)
        except:
            print(inputNeurons)
            print(sens)
            print(interNeurons)
        try:
            sens = sens*weight
        except:
            print(inputNeurons)
            print(sens)
            print(interNeurons)
        #print(sens)
        if end == str(0):
            next
        else:
            temp = endNeuron%len(outputNeurons)
            outputData[temp] += sens
        #print(outputData)
    #print(outputData)
    outputDataMaxed = softmax(outputData)
    outputDataMaxed = outputDataMaxed.tolist()
    maxValue = max(outputDataMaxed)
    #print(inputNeurons)
    #print(outputData)
    pos = outputDataMaxed.index(maxValue)
    if sum(outputData) == 0:
        return None
    else:
        #print(outputNeurons[pos])
        return outputNeurons[pos]