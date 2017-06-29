a = input("Enter a letter")
if len(a)==1 and isinstance(a,str):
    if a in ["a", "e","i","o","u"]:
        print("Its a damn vowel")
    else:
        print("some regular letter!!!")
else:
    print("Enter a single charater ONLY!!!")



