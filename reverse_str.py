#!/usr/bin/python3

a=input("Enter the word/sentence to be reversed...")
l=[]
for i in a:
    l.append(i)
l.reverse()
print(''.join(l))
