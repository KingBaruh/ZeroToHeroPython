
lst = [[]] * 3
lst[0].append(42)
lst[1] += [17]
print(lst[0][0] + lst[2][0])



x = [1, 2, 3]
y = []
for _ in range(2):
    x.append(4)
    y.append(x)
print(y)

s = "python"
t = s
s = s[:3] + "x" + s[3:]
print(t[4], s[5])

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node' = None

def func(x, start=Node(0)):
    start.value += x
    start.next = Node(x)
    return start
a = func(3)
b = func(4)
print(a.value, b.next.value)



def collect(x, lst=[]):
    lst.append(x)
    if x > 0:
        collect(x - 1)
    return lst
result = collect(2)
print(result)



def func1(lst):
    d = {x: i for i, x in enumerate(lst)}
    keys = list(d.keys())
    d[keys[0]] = d[keys[1]]
    return d
print(func1([10, 20, 30])[10])

a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a)
print(b)


def getA_sum(A):
    M, N = len(A), len(A[0])
    A_sum = [[0] * N for _ in range(M)]

    # Bottom-right corner
    A_sum[M - 1][N - 1] = A[M - 1][N - 1]

    # Bottom row
    for j in range(N - 2, -1, -1):
        A_sum[M - 1][j] = A_sum[M - 1][j + 1] + A[M - 1][j]

    # Right column
    for i in range(M - 2, -1, -1):
        A_sum[i][N - 1] = A_sum[i + 1][N - 1] + A[i][N - 1]

    # Rest of the array
    for i in range(M - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            A_sum[i][j] = (A[i][j] + A_sum[i + 1][j] +
                           A_sum[i][j + 1] - A_sum[i + 1][j + 1])

    return A_sum


def subarray_sum(A_sum, pos1, pos2):

    M, N = len(A_sum), len(A_sum[0])
    if pos2[0] == M-1 and pos2[1] == N-1:
        return A_sum[pos1[0]][pos1[1]]

    elif pos2[0] == M-1:
        return A_sum[pos1[0]][pos1[1]] - A_sum[pos1[0]][pos2[1]+1]

    elif pos2[1] == N-1:
        return A_sum[pos1[0]][pos1[1]] - A_sum[pos2[0]+1][pos1[1]]

    return (A_sum[pos1[0]][pos1[1]] - A_sum[pos1[0]][pos2[1]+1] -
            A_sum[pos2[0]+1][pos1[1]] + A_sum[pos2[0]+1][pos2[1]+1])



def find_max_sum(A_sum, m, n):
    M, N = len(A_sum), len(A_sum[0])
    max_sum = float('-inf')
    best_coords = (0, 0, 0, 0)  # i1, j1, i2, j2

    for i in range(M - m + 1):
        for j in range(N - n + 1):
            current_sum = subarray_sum(A_sum, i, j, i + m - 1, j + n - 1)
            if current_sum > max_sum:
                max_sum = current_sum
                best_coords = (i, j, i + m - 1, j + n - 1)

    return best_coords, max_sum


def subsets(nums):
    ans, sol = [], []
    backtrack(nums, len(nums), 0, sol, ans)
    return ans

def backtrack(nums, n, i, sol, ans):
    if i == n:
        ans.append(sol[:])
        return
    # Don't pick nums[i]
    backtrack(nums, n, i + 1, sol, ans)
    # Pick nums[i]
    sol.append(nums[i])
    backtrack(nums, n, i + 1, sol, ans)
    sol.pop()

print(subsets([1, 2, 3,4]))


def s_push(s, node):
    if s is None:
        return node
    node.next = s
    return node

def s_top(s):
    return s

def s_pop(s):
    if s is None:
        return None, None

    new_s = s.next
    s.next = None
    return new_s, s

def isValid(parentheses):
    s = None
    map = { ')':'(' , '}':'{' , ']':'[' }

    for c in parentheses:
        if c not in map:
            s = s_push(s, Node(c))
        else:
            if not s:
                return False
            else:
                s, popped = s_pop(s)
                if popped.value != map[c]:
                    return False

    return True
