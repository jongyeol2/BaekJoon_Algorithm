def solution(s):
    answer = ''
    s_list = []
    for i in s.split():
        s_list.append(int(i))
    answer += str(min(s_list)) + " " + str(max(s_list))
    return answer