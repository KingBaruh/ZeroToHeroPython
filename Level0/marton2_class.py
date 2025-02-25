# %% Question 1
def hanoi_n(n, _from, to, via):
    pass

def hanoi_BH_a(n):
    pass

def hanoi_BH_b(n):
    pass

# %% Question 2
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node' = None

def num_to_list(n):
    pass

def compare_linked_lists(node1, node2):
    pass

def bubble_sort_lists(lst):
    pass

def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# %% Question 3
def climb_combinations(n):
    pass

def tomer_climb_combinations(n, steps):
    pass

# %% Question 4
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    next: 'Node' = None

def s_push(s, node):
    pass

def s_top(s):
    pass

def s_pop(s):
    pass

def isValid(parentheses):
    pass

# %% Question 5
from dataclasses import dataclass


@dataclass
class Node:
    number: int
    next: 'Node' = None


def newSum(list1, list2):
    pass

# %% Question 6
def subsets(nums):
    pass

# %% Question 7
def getA_sum(A):
    pass


def subarray_sum(A_sum, pos1, pos2):
    pass


def find_max_sum(A_sum, m, n):
    pass
