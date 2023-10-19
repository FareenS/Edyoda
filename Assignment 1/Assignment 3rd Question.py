# Q3. Write a program to check if two strings are a rotation of each other?
string1=input("Enter string 1 : ")
string2=input("Enter string 2 : ")
def  rotatestring(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str2
    if str1 in temp:
        return True
    else:
        return False
    
if rotatestring(string1,string2):
    print("Yes!")
else:
    print("No!")