#find duplicates in an array

list=[2,4,5,7,1,13,4]
count=0
number=0

for i in list:
       
    for j in list:
        if (i==j):
            count+=1
if count>2:
    print()


