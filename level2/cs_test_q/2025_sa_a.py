from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node' = None


def hanoi_n(n, _from, to, via):
    if n == 1:
        print(f'{_from} to {to}')
        return

    hanoi_n(n - 1, _from, via, to)
    print(f'{_from} to {to}')
    hanoi_n(n - 1, via, to, _from)


def hanoi_BH_a(n):
    hanoi_n(n, 0, 2, 1)
    hanoi_n(n, 3, 0, 1)
    hanoi_n(n, 2, 3, 1)


def hanoi_BH_b(n):
    hanoi_n(n-1, 0, 2, 1)
    hanoi_n(1, 0, 1, None)
    hanoi_n(n, 3, 0, 1)
    hanoi_n(1, 1, 3, None)
    hanoi_n(n-1, 2, 3, 1)


hanoi_n(3, 1, 3, 2)


def num_to_list(n):
    if n <= 0:
        return None
    new_node = Node(n % 10)
    new_node.next = num_to_list(n // 10)
    return new_node


def compare_linked_lists(node1, node2):
    if not node1 and not node2:
        return 0

    if node1 and not node2:
        return 1

    if not node1 and node2:
        return -1

    result_tail = compare_linked_lists(node1.next, node2.next)
    if result_tail == 0:
        if node1.value > node2.value:
            return 1
        elif node1.value < node2.value:
            return -1
        else:
            return 0

    return result_tail


def bubble_sort_lists(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if compare_linked_lists(lst[j], lst[j + 1]) == 1:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


lst = [num_to_list(4357), num_to_list(1256), num_to_list(3357), num_to_list(1257)]
bubble_sort_lists(lst)
for l in lst:
    print_list(l)