#6. Print multiplication table of a number

num=int(input("enter the number: "))

for i in range(1,13):
    print(str(i)+" * "+str(num)+" = "+str(i*num))