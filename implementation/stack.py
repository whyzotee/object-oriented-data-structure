class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        s = "stack of " + str(self.size()) + " items: "

        for element in self.items:
            s += str(element) + ' '

        return s

s = Stack()

print("\nPush ABCDEF")
for char in "ABCDEF":
    s.push(char)
    print(s.items)

print("Is empty :", s.isEmpty())
print("\nPop until empty")

for i in range(s.size()):
    s.pop()
    print(s.items)

print("\nIs empty :", s.isEmpty())