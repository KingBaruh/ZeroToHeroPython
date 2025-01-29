def stringonacci_loop(n):
    a, b = 'a', 'b'
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(2, n):
        a, b = b, a + b
    return b


#########################################
# שאלות מעקב
#########################################


from dataclasses import dataclass


@dataclass
class Container:
    name: str = 'name'


c1 = Container()
c1.name.upper()
c2 = Container()


#print(c2.name)


def func1(x, lst=[]):
    lst.append(x)
    return lst


d = {}
lst = [1, 2, 3]
d[lst[0]] = lst[1:]
lst[1] += 99
d[lst[0]].append(4)
print(d)
print(lst)

num1 = 1
num2 = 1
tup1 = ()
tup2 = ()
print(num1 is num2)
print(tup1 is tup2)


def add_item(item, collection=set()):
    collection.add(item)
    return collection


print(add_item(1))
print(add_item(2))  # Surprise?

x = 10
lst = [x + y for y in range(3)]
print(lst)

list1 = [[1, 2], [3, 4]]
list2 = list1[:]
list2[0] = [5, 6]
list2[1][0] = 7
print(list1)
print(list2)

x = 5


def foo():
    global x
    print(x)
    x = 10


foo()
print(x)

s = "abcdefgh"
print(s[3::-2][::-1])


#########################################
# שאלות באג בקוד
#########################################


def func10(lst):
    for num in lst:  # bug
        num *= 2
    return lst


def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    lst = unique  # שורה עם באג


def average_wrong(lst):
    sum_lst = 0
    for num in lst:
        sum_lst += num
    return sum_lst / len(lst)  # bug


def make_absolute(lst):
    for num in lst:
        num = abs(num)  # bug
    return lst


def count_char(s, char):
    count = 0
    for c in s:
        if c == char.upper():  # bug
            count += 1
    return count


def search(head, target):
    current = head
    while current.next:
        if current.value == target:  # bug
            return True
        current = current.next
    return False


def tree_height(root):
    if not root:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height)  # bug


#########################################
# שאלות פתוחות
#########################################


def longestOnes(nums, k):
    max_width = 0
    num_zeros = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[left] == 0:
                num_zeros -= 1
            left += 1

        cur_width = right - left + 1
        max_width = max(max_width, cur_width)

    return max_width

# Time Complexity: O(n)
# Space Complexity: O(1)


@dataclass
class Node:
    lst: list
    next: 'Node' = None


def average(lst):
    sum_lst = 0
    for num in lst:
        sum_lst += num
    return sum_lst / len(lst)


def find_avg(head, target):
    if not head:
        return False

    left, right = 0, len(head.lst) - 1

    while left < right:
        cur = head
        mid = (left + right) // 2

        for _ in range(mid):
            cur = cur.next

        avg = average(cur.lst)

        if avg == target:
            return True
        elif avg > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

# Time Complexity: O(n*log(n))
# Space Complexity: O(1)


def find_cycle(arr):

    # Finding cycle length
    width = 1
    while width < len(arr) and arr[width] != arr[0]:
        width += 1

    # Must be a multiple of width or less than width
    if len(arr) % width != 0 or len(arr) == width:
        return False

    j = width

    # Compare segment by segment
    while j < len(arr):
        for k in range(width):
            if arr[j + k] != arr[k]:
                return False
        j += width

    return True  # If all segments match, return True





