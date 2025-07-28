class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

q = Queue()

for char in "ABCDEF":
    q.enQueue(char)
    print("Push",  char, "To Queue:", q.items)
    
print("Size of queue: ",q.size())
