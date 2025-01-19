from dataclasses import dataclass


@dataclass
class Node:
    value: int = 0
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
        else
            cur = cur.next
    return head


#########################################
# Question 2 - do not delete this comment
#########################################

def mergeTwoLists(list1, list2):
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
        "Aviv" : 100
        "Ben" : 67
        "Alice" : 51
    }
    "Discrete Math": {
        "Aviv" : 10
        "Ben" : 63
        "Alice" : 60
    }
    "Linear Algebra":  {
        "Aviv" : 73
        "Ben" : 35
        "Alice" : 78
    }
}


