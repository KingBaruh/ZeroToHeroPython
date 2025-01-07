def removeDuplicates(nums: list[int]) -> int:
    res = 0
    n = len(nums)
    for i in range(n-1):
        if nums[i] != nums[i + 1]:
            nums[res] = nums[i]
            res += 1
    nums[res] = nums[n - 1]
    res += 1
    return res
