def solution(my_string):
    answer = ''
    answer_list = list(my_string)
    for i in answer_list:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            answer += i
    
    return answer


