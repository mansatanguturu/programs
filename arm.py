num=int(input('enter num:'))
l=len(str(num))
temp=num
sum=0
while(num!=0):
    rem=num%10
    sum=sum+(rem**l)
    num=num//10
if(sum==temp):
    print('armstrong')
else:
    print('no')
