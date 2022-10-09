

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next



class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        if self.top is None:
            return 'empty stack'

        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp
    
    # Method that solves the reverse a string function
    def reverse_string(self, string):
        string_reversed = ''
        for letter in string:
            self.push(letter)
        current = self.top
        while current:
            string_reversed += current.value
            current = current.next

        return string_reversed                   
    

if __name__ == '__main__':
    new_stack = Stack()
   
    new_string = 'string'

    print(new_stack.reverse_string(new_string))

