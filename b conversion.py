decimal_number=int(input("Enter a decimal number:"))
binary_number=""
n=decimal_number
while n >0:
    remainder=n%2
    binary_number=str(remainder)+binary_number
    n=n//2
print("The binary form of ", decimal_number,"is",binary_number)