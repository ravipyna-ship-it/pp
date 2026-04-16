#wap to print 1 to 10
for i in range(1,11):
    print(i)

#wap to print 10 to 1
for i in range(10,0,-1):
    print(i) 
#wap to print n to 1
n=int(input("Enter the value"))
for i in range(n,0,-1):
    print(i)
#wap to print squares of 1 to 10
for i in range(1,11):
    print(i+i)
#wap to print squares of 1 to n
n=int(input("Enter the value"))
for i in range(1,n+1):
    print(i*i)    
#wap to print 0 to 5 using for loop
for i in range(6):
    print(i)
    if(i==5): break
else:
    print("Numbers are displayed")    