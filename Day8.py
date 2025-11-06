
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
        self.stack.append(x)
        self.stack.pop()

        return x
