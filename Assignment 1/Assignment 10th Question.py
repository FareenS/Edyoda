# Q10. Write a program to find the smallest number using a stack.

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
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
lenth=int(input('Enter no of items to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1}th number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
print('Smallest number : ',min(stack.get_stack()))