#wap to find grade of a student based on 5 subjects marks using if elif else statement
a=int(input("Enter the marks of subject 1:"))
b=int(input("Enter the marks of subject 2:"))
c=int(input("Enter the marks of subject 3:"))
d=int(input("Enter the marks of subject 4:"))
e=int(input("Enter the marks of subject 5:"))
total=a+b+c+d+e
perc=(otal/500)*100
print("The total marks",total,"percentage is:",perc)
if per>=90:
    print("You get grade A") 
elif per>=80:
    print("You get grade B") 
elif per>=70:
    print("You get grade C") 
elif per>=60:
    print("You get grade D") 
elif per>=50:
    print("You get grade E") 
else:
    print("Fail")                
