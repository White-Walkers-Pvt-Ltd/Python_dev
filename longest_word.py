#!/usr/bin/python3

l=[str(x) for x in input().split()]
v=[]
for i in l:
    v.append(len(i))

print(max(v))    
