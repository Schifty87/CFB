def power(X):
    return X**X;

'''print power(3);'''

def stringMultiply(myString, number):
    return myString*number;

'''print stringMultiply('ryan', 3);'''

def countCodons(DNA):
    count = 0;
    for X in range(0, len(DNA)-2):
        if DNA[X] == 'A' and DNA[X+1] == 'T' and DNA[X+2] == 'G':
            count += 1
    return count

'''print countCodons('ATGCGTATG');'''

def palindromeMaker(input):
    reverse = input[len(input)::-1]
    return input + reverse

print palindromeMaker('ryan');