heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: ")) 
flag = False
for hen  in range(heads):
    cow = heads - hen
    if (2 * hen + 4 * cow == legs):
        print("Number of hens:", hen)
        print("Number of cows:", cow)
        flag = True
        break
if not flag:
    print("No solution found")
  