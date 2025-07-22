str1 = input("enter the string1: ")
str2 = input("enter the string2: ")

a = str1.lower()
b = str2.lower()

c="".join(i for i in a if i!= " ")
d="".join(i for i in b if i!= " ")
c1 = sorted(c)
d1 = sorted(d)
if c1 == d1:
    print("same")
else:
    print("not same")