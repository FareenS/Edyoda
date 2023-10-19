# Q7. Write a program to convert prefix expression to infix expression.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    
    
    def is_empty(self):
        return len(self.items) == 0

string = input("Enter the postfix : ")
 
def postfix(string):
    string=string[::-1]
    res=''
    if len(string)<=1 or string==None:
        return string
    else:
        stack=Stack()
        for strs in string:
            if strs in ["+",'-','*','/']:
                str = "(" + stack.pop() + f"{strs}" + stack.pop() + ")"
                stack.push(str)
            else:
                stack.push(strs)
    while not stack.is_empty():
        res+=stack.pop()
        
    return res 
print('Infix : ',postfix(string))