a=0
b=1
num=int(input('enter a num'))
print(a)
print(b)
for i in range(num-2):
    c=a+b
    print(c)
    a=b
    b=c
