def loadSeq(fileName):
    f = open(fileName)  # open the file
    linesList = f.readlines()  # read in the file as a list of its lines
    f.close()  # close the file
    return linesList

def seq(list):
    L = ''
    for i in list:
        if i[0] != '>':
            L = L + i[:-1]
    return L



list = loadSeq("U81861.fa")
salSeq = seq(list)
print salSeq
print len(salSeq)