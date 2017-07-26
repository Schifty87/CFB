def reverse(S):
    if S=='':
        return ''
    else:
        return S[-1] + reverse(S[:-1])

print reverse('Ryan')