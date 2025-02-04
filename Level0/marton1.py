from dataclasses import dataclass


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


@dataclass
class Node:
    value: int
    next: 'Node' = None

node1 = Node(13)
node1.y = [123]
node2 = Node(11)
node1.next = node2
print(node1.next.y)


def func(x, lst=[]):
    lst.append(x)
    return lst


print(func(1))
print(func(2))

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

def func6(n):
    return n * func6(n - 1) if n != 0 else 0


def func(lst):
    for num in lst:
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


def q_pop(q):
    if q is None:
        return None, None
    new_q = q.next
    q.next = None
    return new_q, q


def compere_to_number(x, y):
    if type(x) is float and type(y) is float:
        return x + y == 0.3
    else:
        return False


def update(st):
    st[:] = "a"


st = "abc"
update(st)


def del_num(lst, idx):
    lst[:] = lst[:idx] + lst[idx + 1:]


def extract_carts(product, lst=[]):
    lst.append(product)
    return lst


betty_cart = extract_carts("Laptop")
yoni_cart = extract_carts("iPhone")

print(betty_cart)
print(yoni_cart)


def duplicate_list(lst):
    for num in lst:
        lst.append(num)


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


def minCoveringIndex(A):
    dict = {}
    max = 0
    for i in range(len(A)):
        if dict.get(A[i], 0) == 0:
            dict[A[i]] = 1
            max = i
    return max


@dataclass
class Node:
    number: int
    next: 'Node' = None


def newSum(list1, list2):
    if not list1 or not list2:
        return None, 0

    res_tail, carry = newSum(list1.next, list2.next)

    current = list1.number + list2.number + carry
    new_node = Node(current % 10)
    new_node.next = res_tail
    return new_node, current / 10


def sort_even_odd(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1
        while left < right and arr[right] % 2 != 0:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


arr = [3, 1, 2, 4, 7, 6, 8, 5]
sort_even_odd(arr)
print(arr)
