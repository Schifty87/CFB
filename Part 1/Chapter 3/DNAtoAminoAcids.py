from aminoAcids import *

'''print aa
print codons'''

def amino(codon):
    for amino in codon:
        index = aa.index(amino)
        print codons[index]

'''amino('S')'''

def codingStrandToAA(DNA):
    list = ''
    for X in range(0,len(DNA),3):
        strand = DNA[X:X+3]
        i=0
        for I in codons:
            if strand in I:
                '''print aa[codons.index(I)]'''
                list += (aa[codons.index(I)])
    print list

'''codingStrandToAA("ATGCAACAGCTC")'''