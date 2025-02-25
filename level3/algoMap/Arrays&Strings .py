from itertools import count


def findClosestNumber(nums: list[int]) -> int:
    a = nums[0]
    for i in nums:
        if abs(i) < abs(a):
            a = i

    if abs(a) in nums:
        return abs(a)
    else:
        return a


def mergeAlternately(word1: str, word2: str) -> str:
    new_word = []
    c1, c2 = 0, 0
    while c1 < len(word1) and c2 < len(word2):
        new_word.append(word1[c1])
        new_word.append(word2[c2])
        c1 += 1
        c2 += 1

    while c1 < len(word1):
        new_word.append(word1[c1])
        c1 += 1

    while c2 < len(word2):
        new_word.append(word2[c2])
        c2 += 1

    return ''.join(new_word)


def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    index = 0
    for ch in t:
        if ch == s[index]:
            index += 1
        if index == len(s):
            return True

    return False


def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        if prices[i] > buy:
            max_profit = max(max_profit, prices[i] - buy)
        else:
            buy = prices[i]

    return max_profit


def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    max_length = float("inf")
    for string in strs:
        max_length = min(len(string), max_length)

    flag = True
    for i in range(max_length):
        ch = strs[0][i]

        for j in range(1, len(strs)):
            if ch != strs[j][i]:
                flag = False

        if flag:
            result += ch
        else:
            return result

    return result


def summaryRanges(self, nums: list[int]) -> list[str]:
    pass