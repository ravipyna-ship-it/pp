a=int(input("Enter the value:"))
b=int(input("Enter the value:"))

a=a&b
print("The bitwise AND is:",a)
a=a|b
print("The bitwise OR is:",a)
a=a^b
print("The bitwise XOR is:",a)
a=~a
print("The bitwise NOT is:",a)
a=a<<2
print("The left shift is:",a)
a=a>>2
print("The right shift is:",a)