def solution(todo_list, finished):
    answer = []
    my_dict = {}
    for i in range(len(todo_list)):
        my_dict[todo_list[i]] = finished[i]
    for k, v in my_dict.items():
        if v == False:
            answer.append(k)
    return answer