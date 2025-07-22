a = input("enter the password")
sp=0
up=0
lw=0
dig=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up = up+1
        elif i.islower():
            lw = lw + 1
        elif i.isdigit():
            dig = dig + 1
        else:
            sp = sp+1
    if(up>0, lw>0, sp>0, dig>0):
        print("good password")
    else:
        print("bad password")        
else:
    print("not a strong password")
                    