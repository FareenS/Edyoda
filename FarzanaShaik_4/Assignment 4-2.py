numbers = [1, 2, 3, 4, 5, 6, 7]

triple = lambda x: x * 3

tripled_numbers = list(map(triple, numbers))

print("Original List:", numbers)
print("Tripled List:", tripled_numbers)