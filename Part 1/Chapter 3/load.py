f = open("goodStuff.txt")
linesList = f.readlines()
f.close()

print linesList

newList=[]  # A new list!
for line in linesList:  # for each line in our linesList...
    newList.append(line[:-1])  # ... slice off the last character and append the truncated string to the newList

print newList