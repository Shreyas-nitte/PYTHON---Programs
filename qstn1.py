a = int(input("Enter the number of blocks: "))
b = int(input("Enter the number of lines: "))
c = int(input("Enter the number of stars: "))

count = 0

for i in range(a):
    print("*****************************************************")
    print("****************BLOCK", i + 1, "****************") 
    for j in range(b):
        for k in range(c):
            print("*", end="")
            count = count + 1 
        print()
    print(count)
    count = count + count
    print(count)
    b -= 1




      
        