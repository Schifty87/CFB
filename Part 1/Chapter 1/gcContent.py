from twoSalDNAs import *

'''assert isinstance(inIsland, object)'''
def gcContent(DNA):
    L = len(DNA);

    count = 0
    for X in range(0, len(outsideIsland)-L):
        if outsideIsland[X:X+L] == DNA:
            count += 1
    return count

S1 = len(outsideIsland)*1.000
print gcContent("ACCGC")/S1