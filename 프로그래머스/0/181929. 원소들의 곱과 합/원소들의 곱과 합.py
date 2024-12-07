def solution(num_list):
    answer = 0
    sum_num_list = 0
    mul_num_list = 1
    
    for i in num_list:
        sum_num_list += i
        mul_num_list *= i
    
    if mul_num_list < sum_num_list**2:
        answer = 1
    
    return answer