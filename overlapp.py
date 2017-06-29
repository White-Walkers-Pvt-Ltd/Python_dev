#!/usr/bin/python3

'''Define a function  overlapping()  that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your  is_member()  function, or the  in  operator, but for the sake of the exercise, you
should (also) write it using two nested for­loops
'''


#a=input("Enter list1")
#b=input("Enter list2")

a=[1,2,3]
b=[5,4]

#count=0
def overlap(l1,l2):
    print(type(l1))
    print(l2)

    count=0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                count=count+1
    return count
count=overlap(a,b)
if count >= 1:
    print("Overlaped",count)
