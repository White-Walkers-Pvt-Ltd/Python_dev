#!/usr/bin/python3
''' ONE OF THE MOST COMPLICATED PROGRAM I EVER WROTE,
The function  max()  from exercise 1) and the function  max_of_three()  from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in
advance how many they are? Write a function  max_in_list()  that takes a list of numbers and returns the largest
one.
'''

l=[int(x) for x in input().split()]

n=len(l)

#for i in range(n):
i=0
def high_chk(i):
    
    for j in range(n):
        if l[i]>=l[j]:
            if j==(n-1):
                print("Highrst:- ",l[i])
        else:
            high_chk(j)
            break
high_chk(i)

