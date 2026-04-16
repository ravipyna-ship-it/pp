"""#wap to print 1 to n
n=int(input("Enter the value"))
for i in range(1,n+1):
    print(i)"""
"""#wap to find sum of 1 to n numbers
n=int(input("Enter the value:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of",n, "numbers=",sum)"""    
"""#wap to find sum of n to 1
n=int(input("Enter the value:"))
sum=0
for i in range(n,0,-1):
    sum=sum+i
print("The sum of",n, "numbers=",sum)"""

"""#wap to find cube of 1 to n
n=int(input("Enter the num:"))
for i in range(1,n+1):
    print(i*i*i)

#wap to find cube of 1 to n and find sum
n=int(input("Enter the value:"))
sum=0
for i in range(1,n+1):
    print(i*i*i)
    sum=sum+(i*i*i)
print("The  sum of 1 to n=",sum)

#wap to get number of digits in a number
n=int(input("Enter the number:"))
count=0
while(n>0):
    digit=n%10
    count=count+1
    n=n//10
print("The digits count in given number=",count)

#wap to get sum of digits in a number
n=int(input("Enter the number:"))
sum=0
while(n>0):
    sum=sum+(n%10)
    n=n//10
print("The digits sum in given number=",sum)

#wap to get product of digits in a number
n=int(input("Enter the number:"))
product=1
while(n>0):
    product=product*(n%10)
    n=n//10
print("The digits product in given number=",product)

#wap to find sum of digits square of number
n=int(input("Enter the number:"))
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)
    n=n//10
print("The sum of digitsquare of num is=",sum) 

#wap to find sum of digits cube of number
n=int(input("Enter the number:"))
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
print("The cube of digitsquare of num is=",sum)

#wap to find sum of digits amstrong or not
n=int(input("Enter the number:"))
n=abs(n)
temp=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if temp==sum:
    print("Number is Amstrong")
else:
    print("Number is Not Amstrong")

#wap to reverse of number
n=int(input("Enter the number:"))
n=abs(n)
rev=0
while(n>0):
    rev=rev*10+(n%10)
    n=n//10
print("Reverse of number is:",rev)

#wap to check number is  palindrome 
n=int(input("Enter the number:"))
n=abs(n)
temp=n
rev=0
while(n>0):
    rev=rev*10+(n%10)
    n=n//10
if temp==rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

#wap to find factorial of a number
n=int(input("Enter the number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("The factorial of number=",fact)

#wap to print even number 1 to n
n=int(input("Enter the number:"))
for i in range(2,n+1,2):
    print(i)

#wap find count of factors of a number
n=int(input("Enter the number:"))
count=0
i=1
while(i<=n):
    if(n%i==0):
        print(i)
        count=count+1
    i=i+1
print("The factors count is=",count)        

#wap to check number is prime or not 
n=int(input("Enter the number:"))
count=0
i=1
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if count==2:
    print("Number is prime")
else:
    print("Number is not prime")

#wap to find simple intrest
p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate of intrest(% per year):"))
t=int(input("Enter the time(in years):"))
si=(p*t*r)/100
total=p+si
print(total)

#wap for celsius to farenheit
celsius=int(input("Enter the temperature in celsius:"))
farenheit=(celsius*9/5)+32
print("{celsius}={farenheit}")

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("")"""
i=1
while(i<6):
    j=1
    while(j<=i):
        print(i,end=" ")
        j=j+1
    print(" ")
    i=i+1        

            
