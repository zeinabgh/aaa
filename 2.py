n1=int(input('enter number 1 :'))
n2=int(input('enter number 2 :'))
n3=int(input('enter number 3 :'))
import math
a=abs(n1-n2)
b=abs(n1-n3)
c=abs(n2-n3)

if a<b and a<c:
    print('min for n1,n2')


if a>b and c>b:
    print('min for n1,n3')


if a>c and b>c:
    print('min for n3,n2')

