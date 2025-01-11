def solution(numbers):
    num_0to9 = {0,1,2,3,4,5,6,7,8,9}
    numbers = set(numbers)
    answer_list = num_0to9.difference(numbers)
    
    answer = sum(answer_list)
    return answer