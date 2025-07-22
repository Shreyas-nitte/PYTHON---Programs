boy = input("Enter boy name: ").lower().replace(" ", "")
girl = input("Enter cute girl name: ").lower().replace(" ", "")

a1 = list(boy)
a2 = list(girl)

for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i] == a2[j]:
            a1[i] = '2'
            a2[j] = '2'
            break

num = 0
for ch in a1 + a2:
    if ch != '2':
        num += 1

print("Total unmatched letters:", num)

ans = ['F', 'L', 'A', 'M', 'E', 'S']
index = 0

while len(ans) > 1:
    index = (index + (num - 1)) % len(ans)
    ans.pop(index)

relations = {
    'F': 'Friends',
    'L': 'Love',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemies',
    'S': 'Siblings'
}

print("The relationship is:", relations[ans[0]])
