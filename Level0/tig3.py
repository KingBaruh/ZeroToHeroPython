from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


def isBalanced(root):
    if not root:
        return True, 0

    balanced, left_height = isBalanced(root.left)
    if balanced is False:
        return False, 0

    balanced, right_height = isBalanced(root.right)
    if balanced is False:
        return False, 0

    if abs(left_height - right_height) > 1:
        return False, 0

    return max(left_height, right_height) + 1, True


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.value

    left_sum = hasPathSum(root.left, targetSum - root.value)
    right_sum = hasPathSum(root.right, targetSum - root.value)

    return left_sum or right_sum


def f(root: Node, i: int, x: int):
    if not root:
        return 0
    if x - i == 0:
        return (1 + f(root.left, i, x - 1)
                + f(root.right, i, x + 1))

    return (f(root.left, i, x - 1)
            + f(root.right, i, x + 1))


def findNode(root, k):
    if not root:
        return None, 0
    if not root.left and not root.right:
        if root.value == k:
            return None, True

    result, left = findNode(root.left, k)

    if result:
        return result, True

    result, right = findNode(root.right, k)

    if result:
        return result, True

    if left and right:
        return root, True

    return None, False

