def solution(nums):
    N = len(nums)/2
    nums = set(nums)
    if len(nums) > N:
        return N
    else:
        return len(nums)

nums = [3,3,3,2,2,4]
print(solution(nums))