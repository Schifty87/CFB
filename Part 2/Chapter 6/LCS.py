def LCS(S1,S2):
    '''return the length of a longest common
    subsequence of strings S1 and S2'''
    if S1 == '' or S2 == '':
        return 0
    elif S1[0] == S2[0]:
        return 1 + LCS(S1[1:],S2[1:])
    else:
        option1 = LCS(S1[1:],S2)
        option2 = LCS(S1,S2[1:])
        return max(option1,option2)

print LCS('DQAQ','SDASQ')