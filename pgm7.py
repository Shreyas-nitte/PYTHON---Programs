notorious = ["DHARSHAN", "ANUJ", "ROHIT"]
names = ["ANU", "DHARSHAN", "ROHIT", "JACK", "PRIYA", "BALA", "RAI", "RAM", "RAJ", "BEN"]
score = [2, 5, 6, 8, 3, 5, 6, 9, 8, 2]
for i in range (10):
    if score[i] > 5 and names[i] not in notorious:
        print(names[i])
   
        
