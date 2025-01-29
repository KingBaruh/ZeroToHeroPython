from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None


def isBalanced(root):
    if not root:
        return True, -1

    balanced, left_height = isBalanced(root.left)
    if balanced is False:
        return False, 0

    balanced, right_height = isBalanced(root.right)
    if balanced is False:
        return False, 0

    if abs(left_height - right_height) > 1:
        return False, 0

    return True, max(left_height, right_height) + 1


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
        return None, False

    if not root.left and not root.right:
        return None, root.value == k

    result, left = findNode(root.left, k)

    if result:
        return result, True

    result, right = findNode(root.right, k)

    if result:
        return result, True

    if left and right:
        return root, True

    return None, left or right


def isValidBST_Wrong(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True

    if root.left and root.left.value >= root.value:
        return False
    if root.right and root.right.value <= root.value:
        return False

    return isValidBST_Wrong(root.left) and isValidBST_Wrong(root.right)


def isValidBST(root):
    return valid(root, float("-inf"), float("inf"))


def valid(node, minimum, maximum):
    if not node:
        return True

    if not (minimum < node.value < maximum):
        return False

    return (valid(node.left, minimum, node.value)
            and valid(node.right, node.value, maximum))


def permute(nums):
    if len(nums) == 1:
        return [nums[:]]

    res = []
    for i in range(len(nums)):
        cur = nums[i]
        remaining = nums[:i] + nums[i + 1:]
        for perm in permute(remaining):
            res.append([cur] + perm)

    return res


def wordSearch(board, word):
    if len(board) == 1 and len(board[0]) == 1:
        return board[0][0] == word

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack((i, j), 0, board, word):
                return True

    return False


def backtrack(pos, index, board, word):
    i, j = pos

    if index == len(word):
        return True

    if board[i][j] != word[index]:
        return False

    char = board[i][j]
    board[i][j] = "#"

    for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        r, c = i + i_off, j + j_off

        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            if backtrack((r, c), index + 1, board, word):
                return True

    board[i][j] = char
    return False
