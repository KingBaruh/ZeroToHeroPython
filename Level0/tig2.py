from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node' = None


#########################################
# Question 1 - do not delete this comment
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
# Question 2 - do not delete this comment
#########################################


def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    current = head

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next

        current = current.next

    return head

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