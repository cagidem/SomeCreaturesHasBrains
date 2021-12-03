from random import randint

def geneCreator(geneNumber):
    genes = []
    for _ in range(geneNumber):
        genes.append(hex(randint(0,4294967295))[2:])
    return genes