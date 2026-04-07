#Count how many times 2 appears in [2, 2, 3, 2]

list1=[2,2,3,2]

count=0
number=2

for i in list1:
    if i==number:
        count+=1
print(str(number)+" found "+str(count)+" times")