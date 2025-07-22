"""display  2 digit numbers divisible by 2,3,5 and 7"""



a= [i for i in range(10,100) if i%2==0 and i%3==0 and i%5==0 and i%7==0 ]
print("2 digit numbers divisible by 2,3,5 and 7 are: ", a)