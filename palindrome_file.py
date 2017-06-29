#!/usr/bin/python3

f=input("Enter the file name:- ")

def is_palim(a):
    if a==a[::-1]:
        print(a)
    else:
        pass


with open(f,'r') as ftemp:
    for line in ftemp:
        for i in line.split():
            is_palim(i)

