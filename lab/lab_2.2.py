###  สร้าง 2D - Linked List
class priNode:
    def __init__(self, data, sec_node=None, next_node=None):
        self.data = data
        self.sec_node = sec_node
        self.next_node = next_node

    def append_secondary(self, sec_data):
        if self.sec_node == None:
            self.sec_node = secNode(sec_data)
        else:
            current_node = self.sec_node

            while current_node.next_node != None:
                current_node = current_node.next_node
            
            current_node.next_node = secNode(sec_data)
    
    def delete_secondary(self, sec_data):
        if self.sec_node.data == sec_data:
            self.sec_node = self.sec_node.next_node
        else:
            current_node = self.sec_node
            while current_node.next_node != None:
                if current_node.next_node.data == sec_data:
                    current_node.next_node = current_node.next_node.next_node
                else:
                    current_node = current_node.next_node

    def __str__(self):
        return self.data

class secNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return self.data

class _2DLinkedList:
    def __init__(self):
        self.head:priNode = None

    def Append_primary(self, pri_data):
        if self.head == None:
            self.head = priNode(pri_data)
        else:
            current_node = self.head

            while current_node.next_node != None:
                current_node = current_node.next_node
            
            current_node.next_node = priNode(pri_data)

    def Delete_primary(self, pri_data):
        if self.head.data == pri_data:
            self.head = self.head.next_node
        else:
            current_node = self.head

            while current_node != None:
                if current_node.next_node == pri_data:
                    current_node.next_node = current_node.next_node.next_node
                else:
                    current_node.next_node = current_node.next_node
    
    def Append_secondary(self, pri_data, sec_data):
        current_node = self.head

        while current_node != None:
            if current_node.data == pri_data:
                current_node.append_secondary(sec_data)
                break
            else:
                current_node = current_node.next_node
    
    def Delete_secondary(self, pri_data, sec_data):
        current_node = self.head

        while current_node != None:
            if current_node.data == pri_data:
                current_node.delete_secondary(sec_data)
                break
            else:
                current_node = current_node.next_node
            
    def Print_List(self):
        current_node = self.head

        while current_node != None:
            print(current_node,end=' : ')

            current_sec_node = current_node.sec_node

            while current_sec_node != None:
                print(current_node.data+current_sec_node.data, end='')
                current_sec_node = current_sec_node.next_node

                if current_sec_node != None:
                    print(',', end='')

            current_node = current_node.next_node

            print()

l1 = _2DLinkedList()

for char in "ABC":
    l1.Append_primary(char)
    l1.Append_secondary(char, '1')
    l1.Append_secondary(char, '2')

l1.Print_List()