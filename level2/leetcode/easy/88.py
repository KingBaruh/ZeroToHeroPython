def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    temp: list = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            temp.append(nums1[i])
            i += 1
        else:
            temp.append(nums2[j])
            j += 1

    while i < m:
        temp.append(nums1[i])
        i += 1

    while j < n:
        temp.append(nums2[j])
        j += 1

    for i in range(len(temp)):
        nums1[i] = temp[i]
