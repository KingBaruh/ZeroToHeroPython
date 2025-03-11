
def find_missing_number(arr: list[99]) -> int:
    full_sum = 0
    for num in range(1, 101):
        full_sum += num

    _sum = 0
    for num in arr:
        _sum += num

    return full_sum - _sum


def find_two_missing_numbers(arr: list[99]) -> int:
    full_sum = 0
    for num in range(1, 101):
        full_sum += num

    _sum = 0
    for num in arr:
        _sum += num

    return full_sum - _sum


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

# Definition for singly-linked list
class ListNode:
     def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

def sortList(head):
    pass


def removeElement(nums: list[int], val: int) -> int:
    nums_size = len(nums)
    i = nums_size - 1

    while i >= 0:
        if nums[i] == val:
            if i != nums_size - 1:
                nums[i] = nums[nums_size - 1]
            nums_size -= 1
        i -= 1

    return nums_size

def removeElement2(nums: list[int], val: int) -> int:
    if len(nums) == 0:
        return 0

    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] == val:
            while nums[j] == val and i < j:
                j -= 1

            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        i += 1

    i = 0
    while i < len(nums):
        if nums[i] == val:
            return i
        i += 1

    return i

def shuffle(arr):
    n = len(arr)
    seed = 20  # Arbitrary number to generate "random-like" indices
    for i in range(n - 1, 0, -1):
        j = (i * seed) % (i + 1)  # Deterministic index
        arr[i], arr[j] = arr[j], arr[i]  # Swap elements

arr_e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(arr_e)
print(arr_e)

def changePassword(s: str, k: int) -> str:
    pass
