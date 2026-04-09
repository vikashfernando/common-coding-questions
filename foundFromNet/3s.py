#Find the maximum number in a list

lst=[3,4,5,6,1,15,6]

number=0

for i in lst:
    if i>number:
        number=i

print(number)