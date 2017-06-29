#!/usr/bin/python3
'''
 Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for­loop, 2) using the higher order function  map() , and 3) using list
comprehensions.
'''

lis=[str(x) for x in input().split()]

def len1(i):
    return len(i)

print(list(map(len1, lis)))
