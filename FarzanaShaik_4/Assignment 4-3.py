numbers = [4, 5, 2, 9]

square = lambda x: x ** 2

squared_numbers = list(map(square, numbers))

print("Original List:", numbers)
print("Squared List:", squared_numbers)