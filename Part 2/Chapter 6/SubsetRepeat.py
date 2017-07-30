def SubsetRepeat(target, numberList):
    if numberList == []:
        return False
    elif target ==0:
        return True
    elif numberList[0] > target:
        return SubsetRepeat(target,numberList[1:])
    else:
        useIt = SubsetRepeat(target - numberList[0],numberList)
        loseIt = SubsetRepeat(target,numberList[1:])
        return useIt or loseIt

print SubsetRepeat(5,[5])