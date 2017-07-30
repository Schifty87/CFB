morsecode =  {'a': '.-' ,
              'b': '-...',
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',
              'z':'--..',
              ' ':'   '}

#print morsecode['j']

def morse(mystring, code):
    x = ''
    for n in mystring:
        x += code[n]
    return x

print morse('a boy', morsecode)