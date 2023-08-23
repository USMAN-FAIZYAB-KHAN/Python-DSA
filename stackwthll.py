from linkedlists import ListNode
class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None
    
    def push(self, val):
        n = ListNode(val)
        n.next = self.top
        self.top = n
    
    def pop(self):
        assert not self.isEmpty(), "Empty Stack"
        x = self.top.data
        self.top = self.top.next
        return x
    
# s = Stack()
# print(s.isEmpty())
# for i in range(9):
#     s.push(i)
# print(s.isEmpty())
# s.top.traverse()
# for i in range(3):
#     print(s.pop())