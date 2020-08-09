def adjust(nums, i):
    lson, rson = 2 * i + 1, 2 * i + 2
    n = len(nums)
    max_idx = i
    if lson < n and nums[lson] > nums[max_idx]:
        max_idx = lson
    if rson < n and nums[rson] > nums[max_idx]:
        max_idx = rson
    if max_idx != i:
        nums[i], nums[max_idx] = nums[max_idx], nums[i]
        adjust(nums, max_idx)
    return nums


def heap_sort(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        nums = adjust(nums, i)
    for i in range(n - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        nums[:i] = adjust(nums[:i], 0)
    print(nums)
    return nums
x = [6,  1 , 2, 7,  9 , 3 , 4  ,5 ,10 , 8]
heap_sort(x)