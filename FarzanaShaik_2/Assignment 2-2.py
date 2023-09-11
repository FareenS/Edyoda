ascii_dict = {}
for char in range(ord('a'), ord('z') + 1):
    ascii_dict[chr(char)] = char
print(ascii_dict)