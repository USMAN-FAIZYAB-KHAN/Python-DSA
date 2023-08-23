class Stack:
    def __init__(self):
        self._elements = list()

    def isEmpty(self):
        return len(self._elements)
    
    def push(self, val):
        self._elements.append(val)
    
    def pop(self):
        assert not self.isEmpty(), "Empty Stack!"
        return self._elements.pop()
    
    