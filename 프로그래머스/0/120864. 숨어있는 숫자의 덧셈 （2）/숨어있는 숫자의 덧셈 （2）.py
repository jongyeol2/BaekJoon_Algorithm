def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    answer_list = my_string.split()
    for i in answer_list:
        answer += int(i)
    return answer