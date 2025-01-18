def next_greater_element(arr):
    stack = []  # Stack to keep indices of elements
    result = [-1] * len(arr)  # Initialize the result array with -1

    for i in range(len(arr)):
        # Pop elements from the stack if the current element is greater
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)  # Push the current index onto the stack

    return result


# Test cases
print(next_greater_element([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]
print(next_greater_element([3, 7, 1, 8, 2, 6]))  # Output: [7, 8, 8, -1, 6, -1]
print(next_greater_element([1, 3, 2, 4]))  # Output: [3, 4, 4, -1]
exit()


def search(lst, id):
    while lst:
        if lst.id == id:
            print("Found")
        lst = lst.next


def insert(lst, new_node):
    if lst is None:
        return new_node

    curr = lst
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return lst


def insert2(di, new_data):
    while di['next']:
        di = di['next']
    di['next'] = new_data


def remove_from_list(lst, id):
    prev = lst

    while lst:
        if lst.id == id:
            if prev is lst:
                lst = lst.next
            else:
                prev.next = lst.next
        prev = lst
        lst = lst.next
    return lst


def merge_lists(lst1, lst2):
    while lst1.next:
        lst1 = lst1.next
    lst1.next = lst2


def insert_sorted(head, value):
    new_node = Node(value)

    if head is None or value < head.value:
        new_node.next = head
        return new_node

    current = head
    while current.next and value > current.next.value:
        current = current.next
    new_node.next = current.next
    current.next = new_node

    return head


def reverse_linked_list_recursive(node):
    if node is None or node.next is None:
        return node

    reversed_list = reverse_linked_list_recursive(node.next)

    node.next.next = node
    node.next = None
    return reversed_list


def find_circle(lst):
    iter = lst
    while (iter):
        if hasattr(iter, 'visited'):
            return True
        iter.visited = True
        iter = iter.next
    return False


def find_circle(lst):
    slow = lst
    fast = lst

    while slow and fast:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def q_push(q, node):
    if q is None:
        return node

    curr = q
    while curr.next:
        curr = curr.next
    curr.next = node
    return q


def q_pop(q):
    if q is None:
        return None, Node

    return q.next, q


# 1->2->3->4
# 4->3
from dataclasses import dataclass
from typing import TypeVar

Node = TypeVar("Node")


@dataclass
class Node:
    value: int
    next: Node = None


node = Node(1, Node(2, Node(3, Node(4, None))))
node = reverse_linked_list_recursive(node)
print(node)
exit()

node = insert_sorted(None, 5)
node = insert_sorted(node, 4)
node = insert_sorted(node, 3)
node = insert_sorted(node, 2)
node = insert_sorted(node, 1)

print(node)
exit()

node = Node(1, 10, 20)
node.next = Node(2, 10, 30, Node(3, 50, 60))
insert(node, Node(4, 40, 40))

node = remove_from_list(node, 3)
print(node)

exit()
node = {'id': 1, 'next': None}
insert2(node, {'id': 2})
print(node)
