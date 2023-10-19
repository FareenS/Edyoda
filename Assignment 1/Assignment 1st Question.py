#1 Write a program to find all pairs of an integer array whose sum is equal to a given number?
arr=[]
lenth= int(input("enter no of items : "))
for i in range(lenth):
    num=int(input(f"enter the {i+1} th number : "))
    arr.append(num)
num= int (input("Enter number for pair : "))
def pairs(arr,num):
    pair=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            # print(arr[i],arr[j],num)
            if arr[i]+arr[j]==num:
                pa=(min(arr[i],arr[j]),max(arr[i],arr[j]))
                pair.add(pa)
    if not pair:
        print ("No Pairs found!",end=" ")
    else:
        return pair
print(pairs(arr,num))