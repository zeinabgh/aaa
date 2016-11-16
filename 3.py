n1=int(input('enter number 1 :'))
n2=int(input('enter number 2 :'))
n3=int(input('enter number 3 :'))
import math

if n1>n2+n3 and n2>n1+n3 and n3>n1+n2:
    print('mosalas ast')

if n1==n2==n3:
    print('motesavi azla')

if n1==n2 or n2==n3 or n1==n3:
    print('motesavi sagheyn')

if pow(n1,2)==(pow(n2,2)+pow(n3,2)) or pow(n3,2)==(pow(n2,2)+pow(n1,2)) or pow(n2,2)==(pow(n3,2)+pow(n1,2)):
    print('ghaemol zavie')
    
