a = (2,5,7,1,3,4,6,8,9,11,32,33,64,31,12,16,65, 'shreyas', 'sachin', 'sanjay', 'suresh', 'siddharth')
even = []
odd = []
string = []
sorted_list = []
for i in a:
    if type(i) == int:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    else:
        string.append(i)
even.sort()
odd.sort()
string.sort()
sorted_list.append(even)
sorted_list.append(odd)
sorted_list.append(string)
print(sorted_list)
    