class SingleNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkedList:
    def __init__(self, node = None):
        self.head = node


S1 = SingleNode(1)
S2 = SingleNode(2)
print(S2)
S1.next = S2
S3 = SingleNode(3)
S2.next = S3

link =SingleLinkedList(S1)
