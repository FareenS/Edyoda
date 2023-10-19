# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse(arr):
    left, right = 0, len(arr) - 1  # Initialize two pointers

    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers towards each other
        left += 1
        right -= 1
    return arr
arr=[]
lenth= int(input("enter no of items : "))
for i in range(lenth):
    num=int(input(f"enter the {i+1}th number : "))
    arr.append(num)
print(reverse(arr))