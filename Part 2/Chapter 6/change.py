def change(amount,denominations):
    '''returns the least number of coins required to make the
    given amount using the list of provided denominations'''
    if amount == 0:
        return 0
    elif denominations == []:
        return float('infinity')
    elif denominations[0]>amount:
        return change(amount,denominations[1:])
    else:
        useIt = 1 + change(amount - denominations[0],denominations)
        loseIt = change(amount,denominations[1:])
        return useIt or loseIt

print change(48,[25,10,5,1])