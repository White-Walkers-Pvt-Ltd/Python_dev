#!/usr/bin/python3

'''
Write a function  filter_long_words()  that takes a list of words and an integer  n  and returns the list of words that are
longer than  n
'''

print("ENter the words..")
l=[str(x) for x in input().split()]
num=int(input("ENter the min length or words to be sorted: "))
v=[]
for i in l:
    v.append(len(i))

V1=[]
for i in range(len(v)):
    if v[i] >= num:
        V1.append(l[i])

print(V1)
