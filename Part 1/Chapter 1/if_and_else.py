def absolute(n):
    return abs(n)

'''print absolute(-2)'''

def palindrome4(input):
    if len(input) != 4:
        return False
    reverse = input[len(input)::-1];
    if input == reverse:
        return True
    return False;

'''print palindrome4('daad')'''


def ORF(DNA):
    if len(DNA) % 3 != 0:
        return False
    '''find the final three codons'''
    end = DNA[len(DNA)-3::]
    if DNA[0:3] == 'ATG':
        if end == 'TGA' or end == 'TAG' or end == 'TAA':
            return True
    return False

print ORF('ATGATGTGAATAG')