### สร้าง Stack ที่ใช้งานได้ 2 ทิศทาง (double head stack)
class Stack:
    def __init__(self):
        self.items = []
    
    def push_left(self, data):
        self.items.insert(0, data)
    
    def push_right(self, data):
        self.items.append(data)
    
    def pop_left(self):
        return self.items.pop(0)

    def pop_right(self):
        return self.items.pop()

    def __str__(self):
        return "items in stack: "+ ' '.join(self.items)

print("==================== Test case ====================")
s1 = Stack()
words = "ABCD"

print("1. Left push, Left pop")

print("Left push")
for char in words:
    print(s1)
    s1.push_left(char)

print(s1)
print("Left pop")
for i in range(len(words)):
    print(s1)
    s1.pop_left()
print(s1)

print("\n2. Right push, Right pop")

print("Right push")
for char in words:
    print(s1)
    s1.push_right(char)

print(s1)
print("Right pop")
for i in range(len(words)):
    print(s1)
    s1.pop_right()
print(s1)

print("\n3. Left push, Right pop")

print("Left push")
for char in words:
    print(s1)
    s1.push_left(char)

print(s1)
print("Right pop")
for i in range(len(words)):
    print(s1)
    s1.pop_right()
print(s1)

print("\n4. Right push, Left pop")
print("Right push")
for char in words:
    print(s1)
    s1.push_right(char)

print(s1)
print("Left pop")
for i in range(len(words)):
    print(s1)
    s1.pop_left()
print(s1)
