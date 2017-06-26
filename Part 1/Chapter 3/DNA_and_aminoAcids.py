def compBase(N):
    if N == 'A':
        return 'T'
    elif N == 'T':
        return 'A'
    elif N == 'C':
        return 'G'
    elif N == 'G':
        return 'C'
    else:
        return 'error'

print compBase('A')


def reverse(s):
    return s[::-1]

print reverse('Ryan')

def reverseComplement(DNA):
    rev = reverse(DNA)
    comp = ''
    for i in rev:
        comp = comp + compBase(i)
    return comp

print reverseComplement("TTGAC")