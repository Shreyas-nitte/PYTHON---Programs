"""teams = []
n = int(input("Enter number of teams: "))
for i in range(n):
    team = []
    team.append(input("Enter team name: "))
    teams.append(team)

matches = []
for i in range(n):
    match = []
    match.append(team"""

teams=[]
n=int(input("Enter no of teams:"))
for i in range(n):
    a=input("enter team name:")
    teams.append(a)
meet=int(input("enter number of meetings:"))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
index=0
print("----------")
for i in match:
     print("Match {} : {} VS {}".format(index,i[0],i[1]))
     index=index+1    
        