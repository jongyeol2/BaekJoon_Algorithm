def solution(nums):
    max_combination = len(nums) / 2
    unique = len(set(nums))
    
    return min(max_combination, unique)