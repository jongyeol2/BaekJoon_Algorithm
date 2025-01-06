def solution(my_string):
    answer = 0
    list = my_string.replace(' - ', ' + -').split(' + ')
    
    for i in list:
        answer += int(i)
    return answer
    
    # return eval(my_string)