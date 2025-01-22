from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node' = None


#########################################
# Question 0 - do not delete this comment
#########################################


def hasCycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow is not fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


#########################################
# Question 1 - do not delete this comment
#########################################


def removeDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.next.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


#########################################
# Question 2 - do not delete this comment
#########################################

def mergeTwoLists(list1, list2):
    # Base cases: if either list is None, return the other list
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Choose the smaller head node and recursively merge the rest
    if list1.value <= list2.value:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


def mergeTwoLists2(list1, list2):
    output = cur = Node(0)

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    cur.next = list1 if list1 else list2

    return output.next
#########################################
# Question 3 - do not delete this comment
#########################################
def twoSum(nums, x):
    seen = {}

    for i, number in enumerate(nums):
        if x - number in seen:
            return seen[x - number], i
        seen[number] = i

    return None

#########################################
# Question 4 - do not delete this comment
#########################################

def getScores1(courses):

    student_scores = {}

    for course, scores in courses.items():
        for student, score in scores.items():

            if student not in student_scores:
                student_scores[student] = []
            student_scores[student].append(score)

    for student, scores in student_scores.items():
        average = sum(scores) / len(scores)
        student_scores[student] = average

    return student_scores


def getScores2(courses):

    student_scores = {}

    for course, scores in courses.items():
        for student, score in scores.items():

            if student not in student_scores:
                student_scores[student] = {}
            student_scores[student][course] = score

    for student, courses in student_scores.items():
        average = sum(courses.values()) / len(courses)
        student_scores[student] = average

    return student_scores


courses = {
    "Calclas 1" : {
        "Aviv" : 100,
        "Ben" : 67,
        "Alice" : 51
    },
    "Discrete Math": {
        "Aviv" : 10,
        "Ben" : 63,
        "Alice" : 60
    },
    "Linear Algebra":  {
        "Aviv" : 73,
        "Ben" : 35,
        "Alice" : 78
    }
}

def fix_list(head):

    # Base case: If the list is empty or has only one node, it is already sorted
    if not head or not head.next:
        return head

    temp_node = None
    current_head = head

    # If the current node is greater than the next node, swap them
    if head.value > head.next.value:
        temp_node = head.next
        head.next = temp_node.next
        temp_node.next = head
        current_head = temp_node

    # Recursive call to fix the rest of the list
    fixed_tail = fix_list(current_head.next)
    current_head.next = fixed_tail

    # After recursion, check again if the current node is out of order if so swap
    if current_head.next and current_head.value > current_head.next.value:
        temp_node = current_head.next
        current_head.next = temp_node.next
        temp_node.next = current_head
        return temp_node

    return current_head

def above_tail_average(head):

    if not head:
        return None
    if not head.next:
        return head.value , 1 , head

    sum_nums , n , tail_list = above_tail_average(head.next)

    if head.value < sum_nums/n:
        return sum_nums , n , tail_list

    head.next = tail_list
    return sum_nums + head.value , n+1 , head

node = Node(8)
node.next = Node(6)
node.next.next = Node(1)
node.next.next.next = Node(3)
node.next.next.next.next = Node(2)
node.next.next.next.next.next = Node(5)
node.next.next.next.next.next.next = Node(1)

tup = above_tail_average(node)
print(tup)

