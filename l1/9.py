#9. Find sum of digits
#Example: 123 → 6


num=2010
num=str(num)
sum=0

for i in num:
    sum+=int(i)

print(sum)