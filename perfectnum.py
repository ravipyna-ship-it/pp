"""n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(n,"is perfect number")
else:
    print(n,"not a perfect number") 

#wap to find spy or not
n=int(input("Enter the number:"))
sum=0
product=1
while n>0:
    d=n%10
    sum=sum+d
    product=product*d
    n=n//10
if sum==product:
    print(sum,"is spy number")
else:
    print(sum,"not a spy number")

foot = int(input("Enter height in foot: "))
inch = int(input("Enter height in inch: "))
total_inches = (foot*12)+inch
cm = total_inches*2.54
print("height of person:", cm)"""

#wap no.of ovels and consonants in a string    
str=input("Enter value:")
v=0
c=0
d=0
for ch in str:
    if ch in "aeiouAEIOU":
        v=v+1
    elif ch.isalpha():
        c=c+1
    elif ch.isdigit():
        d=d+1

print("total vowels",v)
print("total consonants",c)
print("total digits",d)


    