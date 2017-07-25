def differences2(S1, S2):
    if S1=='':
        return 0
    elif S1[0]!= S2[0]:
        return 1 + differences2(S1[1:],S2[1:])
    else:
        return differences2(S1[1:], S2[1:])

print differences2('ATG','TAG')