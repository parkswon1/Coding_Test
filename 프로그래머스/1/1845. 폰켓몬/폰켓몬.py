def solution(nums):
    numSet = set(nums)
    if len(nums) // 2 < len(numSet):
        return len(nums)//2
    return len(numSet)