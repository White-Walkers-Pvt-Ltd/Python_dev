#!/usr/bin/python3

def sum1(a):
    temp=0
    for i in a:
        temp = temp + i
    print(temp)



def mul1(a):
    temp=1
    for i in a:
        temp = temp * i
    print(temp)

l=[]
a = input("Enter the numbers")
while(a != "x"):
    l.append(int(a))
    a = input("Enter num only, To terminate press 'x'")
print(l)

sum1(l)

mul1(l)
