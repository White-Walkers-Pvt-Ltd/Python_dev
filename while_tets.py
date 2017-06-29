#!/usr/bin/python3

l=[]
a = input("Enter the numbers")
while(a != "x"):
    a = input("Enter num only, To terminate press 'x'")
    l.append(a)
l.pop()
print(l)
