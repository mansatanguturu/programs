rev=0
num=int(input('enter num:'))
temp=num
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==temp):
    print('palindrome')
else:
    print('not a palindrome')
