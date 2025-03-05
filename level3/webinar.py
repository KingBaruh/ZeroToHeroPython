def isAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    d = {}

    for ch in str1:
        d[ch] = d.get(ch, 0) + 1

    for ch in str2:
        d[ch] = d.get(ch, 0) - 1

    for ch in d.values():
        if ch != 0:
            return False

    return True


def isValidBST_Wrong(root):
    if not root:
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

    return valid(node.left, minimum, node.value) and valid(node.right, node.value, maximum)


def eval_s(s):
    sum_s = 0
    mul_s = 1
    n = 0  #cur_num
    for c in s:
        if c.isdigit():
            n = n * 10 + int(c)
            continue
        # + or *
        mul_s *= n
        n = 0
        if c == '+':
            sum_s += mul_s
            mul_s = 1

    return sum_s + mul_s * n
