#!/usr/bin/python3
import random
'''
Game- word scrambler
'''
def scambl(a):
    l=['*' for x in range(len(a))]
    hist=[]
    for i in a:
        while '*' in l:
            index=random.randrange(len(a))
            if index not in hist:
                hist.append(index)
                l[index]=i
                break
    return l

wordset=['ambulant','american','david','serendipity','washington','tajmahal','tagore','saroj','dharma']
word1=wordset[random.randrange(len(wordset))]
opp=''.join(scambl(word1))
countr=1
#print(word1)
#print(''.join(opp))
print("You will be provided a scrambled word. Enter its corrected version")
print("There it is....",opp)

guess= input("Enter your guesses")
while guess != word1:
    countr += 1
    guess= input("Nope!!!Try another guess")

print("Congratz!!! You have got the answers in no. guesses",countr)


