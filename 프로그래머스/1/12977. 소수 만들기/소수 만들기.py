def is_prime(nums):
    sum_n = sum(nums)
    
    if sum_n < 2:
        return 0
    
    for i in range(2, int(sum_n**0.5) + 1):
        if sum_n % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    n = len(nums)
    num_3 = []
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                num_3.append([nums[i], nums[j], nums[k]])

    for i in num_3:
        answer += is_prime(i)
    
    return answer