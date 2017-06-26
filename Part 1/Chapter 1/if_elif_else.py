def ORFadvisor(DNA):
    message = []
    if DNA[0:3] != 'ATG':
        message.append('The first three bases are not ATG')
    end = DNA[len(DNA) - 3::]
    if end != 'TGA' and end != 'TAG' and end != 'TAA':
        message.append('The last three bases are not a stop codon')
    if len(DNA)%3 != 0:
        message.append('The string is not of the correct length')

    if len(message) == 0:
        return 'This is an ORF'
    else:
        return message

'''print ORFadvisor('ATGATAA')'''

def friendly(greeting):
    if greeting[0:5]=='Hello' or greeting[0:2] == 'hi':
        return 'nice to meet you'
    elif greeting[len(greeting)-1] == '?':
        return 'good question!'
    else:
        return 'I am sorry, but I did not understand you'

print friendly('who are you?')