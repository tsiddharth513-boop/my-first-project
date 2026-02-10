print("=== Simple Calculator ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)

if b == 0:
    print("Quotient = Cannot divide by zero")
else:
    print("Quotient =", a / b)

input("Press Enter to exit...")
    
