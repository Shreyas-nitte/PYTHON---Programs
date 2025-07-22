a = int(input("Enter a number: "))
b=[500,200,100,50,20,10,5,2,1]
fivehundrednotes=0
twohundrednotes=0
hundrednotes=0  
fiftynotes=0
twentynotes=0
tennotes=0
fivenotes=0
twonotes=0
onenotes=0
for i in  b:
    while a >= i:
        a=a-i
        fivehundrednotes+=1
    while a >= i:
        a=a-i
        twohundrednotes+=1
    while a >= i:
        a=a-i
        hundrednotes+=1
    while a >= i:
        a=a-i
        fiftynotes+=1
    while a >= i:
        a=a-i
        twentynotes+=1
    while a >= i:
        a=a-i
        tennotes+=1
    while a >= i:
        a=a-i
        fivenotes+=1
    while a >= i:
        a=a-i
        twonotes+=1
    while a >= i:
        a=a-i
        onenotes+=1
print("500 notes:", fivehundrednotes)
print("200 notes:", twohundrednotes)        
print("100 notes:", hundrednotes)
print("50 notes:", fiftynotes)
print("20 notes:", twentynotes)
print("10 notes:", tennotes)
print("5 notes:", fivenotes)
print("2 notes:", twonotes)
print("1 notes:", onenotes)
        
    