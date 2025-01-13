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


def product_except_self(nums: list[int]) -> list[int]:
    multi = 1
    zero_count = 0
    result = []

    # Compute the total product of non-zero elements and count zeroes
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            multi *= num

    # If more than one zero exists, the result is all zeroes
    if zero_count > 1:
        return [0] * len(nums)

    # Build the result
    for num in nums:
        if zero_count == 1:
            # If there's exactly one zero, only the position of zero gets the product
            result.append(multi if num == 0 else 0)
        else:
            # Normal case, compute product except self
            result.append(multi // num)  # Use integer division
    return result


def create_zero_matrix(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

