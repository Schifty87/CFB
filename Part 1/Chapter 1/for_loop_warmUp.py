def count(letter, string):
    count = 0
    for X in string:
        if X == letter:
            count += 1
    return count

print count('z', 'zyzzyzus')