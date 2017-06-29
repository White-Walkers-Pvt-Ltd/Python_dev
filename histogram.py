#!/usr/bin/python3

#l=[]
#a = input("Enter the numbers")
#while(a != "x"):
#    l.append(int(a))
#    a = input("Enter num only, To terminate press 'x'")

l = [int(x) for x in input().split()]
print(l)
for i in l:
    l1=[]
    for j in range(i):
        l1.append("*")
    print(''.join(l1))
