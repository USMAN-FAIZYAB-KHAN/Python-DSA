class DLNode:
    def __init__(self, val) -> None:
        self.data = val
        self.right = None
        self.left = None

    def insertRight(self, val):
        prev = self
        middle = DLNode(val)
        next = self.right
        middle.right = next
        middle.left = prev
        prev.right = middle
        if next is not None:
            next.left = middle
        
    def insertLeft(self, val):
        # r q p
        p = self
        q = DLNode(val)
        r = p.left
        q.right = p
        q.left = r
        p.left = q
        if r is not None:
            r.right = q

    def delete(self):
        prev = self.left
        next = self.right
        if prev is not None:
            prev.right = next
        if next is not None:
            next.left = prev
        if prev is None:
            return next
        return prev
    
    def __len__(self):
        count = 0
        curr = self
        while curr is not None:
            count += 1
            curr = curr.right
        curr = self.left
        while curr is not None:
            count += 1
            curr = curr.left
        return count
    
    def traverse(self):
        current = self
        # go all the way to the left
        while current.left is not None:
            current = current.left
        # Now traverse the list by going right
        print("X <- ", end="")
        while current.right is not None:
            print(current.data, end=" <-> ")
            current = current.right
        print(current.data, "-> X")
        print()

    def search(self, target):
        b = self
        while b is not None and b.data != target:
            b = b.right
        if b is not None:
            return b
        b = self.left
        while b is not None and b.data != target:
            b = b.left
        return b
    
def buildDlRight(values):
    assert len(values) > 0, "No values present"
    c = DLNode(values[0])
    for i in range(1, len(values)):
        c.insertRight(values[i])
        c = c.right
    return c

def buildDlLeft(val):
    assert len(val) > 0, "No values"
    c = DLNode(val[0])
    for i in range(1, len(val)):
        c.insertLeft(val[i])
        c = c.left
    return c

# l = buildDlLeft([1, 2, 3, 4, 5, 6, 7, 8, 9])
# l.traverse()