#5. Find sum of numbers from 1 to n

sum=0
num=int(input("enter the number: "))

for i in range(1,(num+1)):
    sum+=i
print("sum = "+str(sum))

