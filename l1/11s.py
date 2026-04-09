#8. Reverse a number (correct way)
#Example: 123 → 321

num=123
reveredNum=0

while num>0:
    digit=num%10
    reveredNum=reveredNum*10+digit
    num//=10

print(reveredNum)
