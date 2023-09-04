# Initialize the first two Fibonacci numbers

num1 =0
num2 =1
next_number = num2

# Print the first Fibonacci number (0)
print(num1, end='')

# Generate and print the Fibonacci series up to 50
while num2 <=50:
    print(num2, end='')
    num1, num2 = num2, num1 + num2