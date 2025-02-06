from dataclasses import dataclass


#########################################
# Test 1 - Question 1
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


#########################################
# Test 1 - Question 2
#########################################

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
        mid = (left + right) // 2
        cur = head

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


#########################################
# Test 2 - Question 1
#########################################


@dataclass
class Node:
    number: int
    next: 'Node' = None


def newSum(list1, list2):
    pass


#########################################
# Test 2 - Question 2
#########################################

def sort_even_odd(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1

        while left < right and arr[left] % 2 != 0:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


#########################################
# Test 2 - Question 3
#########################################

def backtrack(pos, index, board, word):
    i, j = pos

    if index == len(word):
        return True

    if board[i][j] != word[index]:
        return False

    char = board[i][j]
    board[i][j] = '#'

    for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        r, c = i + i_off, j + j_off

        if 0 <= r < len(board) and 0 <= c < len(board[i]):
            if backtrack((r, c), index + 1, board, word):
                return True

    board[i][j] = char
    return False


def wordSearch(board, word):
    if board is None:
        return False
    if len(board) == 1 and len(board[0]) == 1:
        return board[0][0] == word

    for i in range(len(board)):
        for j in range(len(board[i])):
            if backtrack((i, j), 0, board, word):
                return True
    return False


def duplicate_list(lst):
    for i in range(len(lst)):
        lst.append(lst[i])
