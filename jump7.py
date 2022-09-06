a=0
while a<100:
    a=a+1
    b=a%7
    c=a%10
    d=a//10
    if b ==0:
        continue
    if c ==7:
        continue
    if d ==7:
        continue
    print(a)
