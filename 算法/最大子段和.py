def maxSubSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    b, sub_sum = 0, float('-inf')
    for x in nums:
        if b > 0:
            b += x
        else:
            b = x
        if b > sub_sum: sub_sum = b
    return sub_sum