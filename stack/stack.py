class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.heigth = 1

    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def push(self, value):
        new_node = Node(value)
        if self.heigth == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.heigth += 1
        return True
    
    def pop(self):
        if self.heigth == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.heigth -= 1
        return temp.value



teste = Stack(4)
teste.push(1)
teste.push(7)
x = teste.pop()
teste.print_stack()
print("pop: ", x)