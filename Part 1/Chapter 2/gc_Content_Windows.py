from salGenomicRegion import *

def gcWin(DNA,stepLen):
    list = []

    for X in range(0,len(DNA),stepLen):
        count = 0
        '''determine how much of this has G or C'''
        slice = DNA[X:X+(stepLen)]
        for i in slice:
            if i == 'G' or i == 'C':
                count += 1
        count = count*1.00000

        print(count/stepLen)

slice = salDNA
gcWin(slice,10000)