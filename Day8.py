
class Stack:
    def __init__(self):
       self.stack = []


    def push(self,data):
        self.stack.append(data)

    def pop(self):
        popped_item = self.stack.pop()
        return popped_item

    def is_empty(self):
        if len(self.stack ) == 0:
              return True 
        else:
            return False
        
    def return_string(self,x: str):
       reversed_str= ''

       for char in x:
           self.push(char)
           
       while not self.is_empty():
           reversed_str += self.pop()

       return reversed_str
    
stack = Stack()
text = input("Enter a text to reverse: ")
RESULT =  stack.return_string(text)
print(f"Result: {RESULT}")
