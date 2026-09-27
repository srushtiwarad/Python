#Factors
"""
n=10
for i in range (1,n+1,1):
    print(i)
"""
    
#real factors
"""
n=10
for i in range(1,n+1,1):
   if n % i == 0:    
       print(i) 
"""

#prime numbers
"""
for n in range(1,11):
    count=0
    for i in range(1,n+1,1):
        if n % i == 0:
            count=count+1
    if count==2:
        print(n, "is a prime number")
    else:
        print(n,"not prime number")
"""

#Common Factors
"""
n=10  
m=20

for i in range (1,n+1,1):
    if n % i == 0 and m % i == 0:
        print(i)
"""

#HCF
"""
n=10
m=20
list=[]
for i in range (1,n+1,1):
    if n%i==0 and m%i==0:  
        list.append(i)
hcf=max(list)
print(hcf)
"""

#LCM
"""
n=10                                                                    [20]
m=20                                                                    [20, 40]
m=20                                                                    [20, 40, 60]
list=[]                                                                 [20, 40, 60, 80]
for i in range (1,n*m+1,1):                                             [20, 40, 60, 80, 100] 
    if i%n==0 and i%m==0:                                               [20, 40, 60, 80, 100, 120]
        list.append(i)                                                  [20, 40, 60, 80, 100, 120, 140]
        print(list)                                                     [20, 40, 60, 80, 100, 120, 140, 160] 
                                                                        [20, 40, 60, 80, 100, 120, 140, 160, 180]
                                                                        [20, 40, 60, 80, 100, 120, 140, 160, 180,200]
"""
#or
"""n=10
m=20
list=[]
for i in range (1,n+1,1):
    if n%i==0 and m%i==0:
        list.append(i)
hcf=max(list)
lcm=(n*m)/hcf
print(lcm)
"""

#Successive Calculations
#sum of n natural num
"""
n=10
sum=0
for i in range (1,n+1,1):
    sum=sum+i
print(sum)        
"""
#Average
"""
n=10
sum=0
for i in range (1,n+1,1):
    sum=sum+i
avg=sum//n
print(avg)
"""
#Factorial
"""
n=10
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print(fact)
"""
#Sum of first 10 even and odd number

"""
n=10
sum=0
for i in range (1,2*n+1,2): #even
    sum=sum+i
print(sum) 
""" 
""" 
n=10
sum=0
for i in range(1,2*n,2): #odd
    sum=sum+i
print(sum)  
"""
#Gensis and destruction
"""
n=0
a=[4,3,2,1]    #gensis
for i in a :
    n=n*10
    n=n+i
print(n)
"""
"""
n=4321
while n!=0:    #destruction
    r=n%10
    n=n//10
    print(r, n)
"""
"""
n=54321     #length of number
count=0
while n!=0:
    r=n%10
    n=n//10
    count=count+1
print(count)
"""
"""
n=4321              #sum of digits
sum=0
while n!= 0:
    r=n%10
    n=n//10
    sum=sum+r
print(sum)
"""
n=54321
m=0
while n!=0:
    r=n%10
    n=n//10
    m=m*10
    m=m+r
print(m)