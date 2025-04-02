def solution(t, p):
    answer = 0
    len_p = len(p)
    t_list = []
    
    for i in range(len(t)):
        if len(t[i:i+len_p]) == len_p:
            t_list.append(t[i:i+len_p])
    
    for i in t_list:
        if int(i) <= int(p):
            answer += 1
    # 이게 외않되? 아 ㄹㅇ;
    return answer