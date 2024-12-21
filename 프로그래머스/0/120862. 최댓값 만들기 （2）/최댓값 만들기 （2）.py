def solution(numbers):
    sort_num = sorted(numbers)
    answer = max(sort_num[-1]*sort_num[-2], sort_num[0]*sort_num[1])
        
    return answer