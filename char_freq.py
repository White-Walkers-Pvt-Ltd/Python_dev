#!/usr/bin/python3

'''
Write a procedure  char_freq_table()  that, when run in a terminal, accepts a file name from the user, builds a
frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen
'''
import string

fin=input("ENter the file name-..")
alfa=string.ascii_lowercase[:]
l=[0 for x in range(26)]
def countr(a):
    for i in a:
        if i in alfa:
            l[alfa.index(i)] +=1

with open(fin,'r') as ftemp:
    for line in ftemp:
        for word in line.split():
            countr(word)

print(l)        
