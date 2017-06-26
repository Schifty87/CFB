def countLength(DNAlist, length):
    count = 0
    for X in DNAlist:
        if len(X) == length:
            count += 1
    return count

print countLength(["ATA", "ATCG", "TTT", "A"], 4)

def getLength(DNAlist, length):
    list = []
    for X in DNAlist:
        if len(X) == length:
            list.append(X)
    return list

print getLength(["AACC", "A", "T"], 1)


def factorial(n):
    num = 1
    for X in range(1,n+1):
        num = num*X
    return num

print factorial(3)