#!/usr/bin/python3

import string

pang=input("Enter the text")
pang=pang.lower()
count =0

for i in string.ascii_lowercase[:]:
    if i not in pang:
        count=count+1

if count == 0:
    print("Its Pangram!!!")
else:
    print("Nope..its not.")



