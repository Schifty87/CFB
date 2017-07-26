def complimentSymbol(symbol):
    if symbol=='A':
        return 'T'
    elif symbol=='T':
        return 'A'
    elif symbol=='G':
        return 'C'
    elif symbol=='C':
        return 'G'

def compliment(S):
    if S=='':
        return''
    else:
        return complimentSymbol(S[0]) + compliment(S[1:])


print compliment('AATG')