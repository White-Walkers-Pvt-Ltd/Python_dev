#!/usr/bin/python3

'''
Write a function  translate()  that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is,
double every consonant and place an occurrence of  "o"  in between. For example,  translate("this is fun")  should
return the string  "tothohisos isos fofunon" .
'''
def transl8r(a,b):
    print(a)
    for i in a:
        if i not in ["a", "e","i","o","u"," "]:
            b.append(i)
            b.append("o")
            b.append(i)
        else:
            b.append(i)
    print(''.join(b))

a = input("Enter the message..")
b=[]
transl8r(a,b)
