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
for n in range(1,11):
    count=0
    for i in range(1,n+1,1):
        if n % i == 0:
            count=count+1
    if count==2:
        print(n, "is a prime number")
    else:
        print(n,"not prime number")