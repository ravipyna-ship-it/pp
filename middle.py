#wap to find the middle among three numbers
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
#wap to find the middle among three numbers
if(a<b and a>c) or (a>b and a<c):
    print("a is middle number",a)
elif(b>a and b<c)or (b<a and b>c):
    print("b is midle number",b)
else:
    print("c is middle number")    