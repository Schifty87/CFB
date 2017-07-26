def subset(target,numberList):
    '''returns TRUE if there exists a subset of numberList
    that adds up to target and returns False Otherwise'''
    if target == 0:
        return True
    elif numberList == []:
        return False
    elif numberList[0]>target:
        return subset(target, numberList[1:])
    else:
        useIt = subset(target-numberList[0], numberList[1:])
        loseIt = subset(target,numberList[1:])
        return useIt or loseIt

print subset(6,[7,2,5,4])