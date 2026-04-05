#8. Reverse a number
#Example: 123 → 321

lst1=[]
num="2026"

for i in num:
    lst1.append(i)

lst2=lst1[-1::-1]

for j in lst2:
    print(j, end="")



print(" ")
print("*"*40)
print("easiest way")



num1=2026
num1=str(num1)
reversedNum=num1[-1::-1]
print(int(reversedNum))