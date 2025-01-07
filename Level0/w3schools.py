# O(m * log(n))
def find_b(arr: list[list[int]], b: list[int]) -> int:
    value_b = 0
    for i in range(len(b)):
        value_b += b[i] * 2**i

    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        value_i = 0
        for j in range(len(arr[mid])):
            value_i += arr[mid][j] * 2 ** j
        if value_i == value_b:
            return mid
        elif value_i < value_b:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_to_string(root: Node, arr: list[str]) -> None:
    if root is None:
        return None
    arr.append('(')
    tree_to_string(root.left, arr)
    arr.append(str(root.value))
    tree_to_string(root.right, arr)
    arr.append(')')


def isCover(string: str, cover: str) -> bool:
    hist = [0]*255
    c_hist = [0]*255
    for i in range(len(cover)):
        hist[ord(cover[i])] += 1
        c_hist[ord(cover[i])] += 1
    start, end, latest_good_index = 0, 1, 10
