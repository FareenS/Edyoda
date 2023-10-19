# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def closed(string):
    temp={'(':0,')':0}
    for c in string:
        if c == "(" :
            temp['(']+=1
        if c==")":
            temp[')']+=1

        
    return temp['(']%2==0 and temp[')']%2==0

string = input('Enter the string : ')
print(closed(string))