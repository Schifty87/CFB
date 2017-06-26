def countPattern(pattern,string):
    count = 0
    L = len(pattern)
    for X in range(0,len(string)-(L-1)):
        if string[X:X+L] == pattern:
            count += 1
    return count

print countPattern("aa", "aaabaaa")
