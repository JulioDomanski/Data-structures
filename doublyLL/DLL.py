class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node

        self.length += 1
        return True
    
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before
       


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    

    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp


    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
            

x = DoublyLinkedList(0)
x.append(1)
x.append(2)
x.insert(2, 3)
x.remove(2)

x.print_list()

