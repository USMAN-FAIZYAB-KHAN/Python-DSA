class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def insert(self, value):
        node = ListNode(value)
        node.next = self.next
        self.next = node

    def delete(self):
        item = None
        if self.next is not None:
            tmp = self.next
            item = tmp.data
            self.next = tmp.next
        return item

    def __len__(self):
        curr = self
        i = 0
        while curr is not None:
            i += 1
            curr = curr.next
        return i

    def traverse(self):
        curr = self
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def search(self, target):
        a = self
        if a.data == target:
            return [True, None, a]
        b = a.next
        while b is not None and b.data != target:
            a = a.next
            b = b.next
        return [b is not None, a, b]

    def circularize(self):
        a = self
        while a.next is not None:
            a = a.next
        a.next = self

    def linearize(self):
        a = self
        while a.next is not self:
            a = a.next
        a.next = None

    def traverse_circular(self):
        current = self
        while current.next is not self:
            print(current.data, end=" ")
            current = current.next
        print(current.data, end=" ")
        print()

def insAfter(head: ListNode, x, val):
    res = head.search(x)
    if res[0] == True:
        res[2].insert(val)

def insBefore(head:ListNode, x, val):
    res = head.search(x)
    if res[0] == True:
        if res[2] is head:
            n = ListNode(val)
            n.next = head
            head = n
        else:
            res[1].insert(val)
    return head

def delNode(head:ListNode, x):
    res = head.search(x)
    if res[0] == True:
        if res[2] is head:
            head = head.next
        else:
            res[1].delete()
    return head

def instail(head, val):
    if head is None:
        return ListNode(val)
    current = head
    while current.next is not None:
        current = current.next
    n = ListNode(val)
    current.next = n

def buildList(val):
    assert len(val) > 0, "No items"
    head = ListNode(val[0])
    current = head
    for i in range(1, len(val)):
        current.insert(val[i])
        current = current.next
    return head

def buildlist():
    head = None
    while True:
        val = input("Enter value or Just Enter to exit: ")
        try:
            if val == "":
                return head
            else:
                val = int(val)

            if head is None:
                head = ListNode(val)
                b = head
            else:
                b.insert(val)
                b = b.next
        except:
            print("Enter correct value")

    



# head = ListNode(0)
# curr = head
# for i in range(5):
#     n = ListNode(i+1)
#     curr.next = n
#     curr = n
# head.traverse()
# head.circularize()
# head.next.next.traverse_circular()