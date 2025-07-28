class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self, head = None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            tail = self.head
            self.size = 1

            while tail.next != None:
                tail = tail.next
                self.size += 1
            self.tail = tail

    def append(self, data):
        ptr = Node(data)

        if self.head is None:
            self.head = ptr
        else:
            tail = self.head

            while tail.next != None:
                tail = tail.next
            
            tail.next = ptr
            
        self.size += 1
    
    def insertAfter(self, data, char):
        ptr = Node(data)
        
        tail = self.head

        while tail is not None:
            if tail.data == char:
                ptr.next = tail.next
                tail.next = ptr

                if tail == self.tail:
                    self.tail = ptr

                self.size += 1
                break

            tail = tail.next
    
    def deleteAfter(self, char):
        tail = self.head

        while tail is not None:
            if tail.data == char:
                tail.next = tail.next.next
                self.size -= 1

            tail = tail.next
    
    def addHead(self, data):
        self.head = Node(data, self.head)

    def deleteHead(self):
        self.head = self.head.next
    
    def __str__(self):
        linked_list = ""
        ptr = self.head

        while ptr != None:
            linked_list += f"|{ptr.data}|{ptr.next}|"
            ptr = ptr.next

            if(ptr != None):
               linked_list += "-->" 

        return linked_list

l = LinkedList()

for char in "ABCDEF":
    l.append(char)

push_list = ['X', 'Y', 'Z']
insert_after_char = 'C'

for char in push_list:
    l.insertAfter(char, insert_after_char)
    insert_after_char = char

    print("Insert", char)
    print(l, sep='', end="\n\n")

print("Additional")

l2 = LinkedList()

for i in "12345":
    l2.append(i)
print(l2, sep='', end="\n\n")

print("delete node after 2")
l2.deleteAfter('2')
print(l2, sep='', end="\n\n")

print("insert 2.5 after 2")
l2.insertAfter('2.5','2')
print(l2, sep='', end="\n\n")

print("delete head")
l2.deleteHead()
print(l2, sep='', end="\n\n")

print("add 0 to head")
l2.addHead('0')
print(l2, sep='', end="\n\n")