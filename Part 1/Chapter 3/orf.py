
#find all open reading frames
#must start with ATG and end with stop codon
def restOfORF(DNA):
    array = []
    for X in range(0,len(DNA)):
        if DNA[X:X+3] == 'ATG':
            list = ''
            for I in range(X, len(DNA),3):
                #print DNA[I:I+3]
                #kill loop if stop codon found AND length is greater than 'ATG'
                if DNA[I:I+3] in ['TAG', 'TGA', 'TAA'] and len(list)>3:
                    array.append(list)

                    break
                else:
                    list += DNA[I:I+3]
    return array




DNA="CAGCTCCAATGTTTTAACCCCCCCC"

'''print restOfORF(DNA)'''


#instead of incrementing one by one,
#increment by three right off the bat
def oneFrame(DNA):
    array = []
    for X in range(0, len(DNA), 3):
        list = ''
        if DNA[X:X + 3] == 'ATG':
            for I in range(X, len(DNA), 3):
                if DNA[I:I + 3] in ['TAG', 'TGA', 'TAA'] and len(list) > 3:
                    array.append(list)
                    break
                else:
                    list += DNA[I:I + 3]
    return array

print oneFrame(DNA[2:])

