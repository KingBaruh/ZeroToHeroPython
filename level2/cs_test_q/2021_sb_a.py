class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def split_list(l: Node, l1:Node, l2:Node) -> int :
    if not l1:
        l1, l2 = None, None
        return -1
    max_tail = split_list(l.next, l1, l2)

    if l.value >= max_tail:
        l.next = l
        l1 = l
