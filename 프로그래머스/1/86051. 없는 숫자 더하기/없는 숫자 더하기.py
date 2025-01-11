def solution(numbers):
    num_0to9 = {0,1,2,3,4,5,6,7,8,9}
    numbers_set = set(numbers)
    
    answer_set = num_0to9 - numbers_set
    answer = sum(answer_set)
    return answer