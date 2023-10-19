# Q4. Write a program to print the first non-repeated character from a string?

string=input("Enter string : ")
def repeat(string)->str:
    temp={}
    for i in string:
        temp[i]=1+temp.get(i,0)
    for i in string:
        if temp[i]==1:
            return i
print('Non-repeated character : ',repeat(string))