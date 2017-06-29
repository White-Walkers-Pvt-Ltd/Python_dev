#!/usr/bin/python3

'''
Your task in this exercise is to implement an encoder/decoder of ROT­13. Once you're done, you will be able to
read the following secret message:
   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT­13 program will be able to both encode and decode texts
written in English.
'''

import string
inp=input("Enter the mesg..")
n=13

inp = inp.lower()
a=string.ascii_lowercase[:]
dictt={a[i]:a[(i+n)%26] for i in range(26)}
l=[]
for i in inp:
    if i in string.ascii_lowercase[:]:
        l.append(dictt[i])
    else:
        l.append(i)

print(''.join(l))
