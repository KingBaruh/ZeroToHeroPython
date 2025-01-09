class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head: Node) -> Node | None:
    # Base case: if the list is empty or has one node, return the head
    if head is None or head.next is None:
        return head

    # Recursively reverse the rest of the list
    new_head = reverse(head.next)

    # Reversing the links
    head.next.next = head  # Point the next node's next to the current node
    head.next = None  # Set the current node's next to None

    return new_head  # Return the new head of the reversed list


def reverse_half(head: Node, x: list[int]) -> Node | None:

    x[0] += 1
    if head.next is None or head is None:
        return head
    new_head = reverse_half(head.next, x)
    x[0] -= 2

    if x[0] > 0:  # Reverse the second half
        head.next.next = head
        return new_head
    if x[0] == 0:  # Midpoint, stop reversal
        head.next.next = None
        head.next = new_head

    return head

def arrays_of_indices(A: list[int]) -> list[list[int]]:
    hist = [0] * len(A)
    for i in range(len(A)):
        hist[A[i]] += 1

    main_arr = []
    for i in range(len(A)):
        if hist[i] > 0:
            main_arr.append([0]*hist[i])
    for i in range(len(A)-1, -1, -1):
        main_arr[A[i]][hist[A[i]]-1].append(i)
        hist[A[i]] -= 1
    return main_arr

