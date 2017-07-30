def numGame(numList):
    if numList == []:
        return 0

    else:
        L1 = numList[0] + numGame(numList[1:])
        L2 = numList[1] + numGame(numList[2:])
        return max(L1,L2)

print numGame([1,2,3,4,5,6,7])
