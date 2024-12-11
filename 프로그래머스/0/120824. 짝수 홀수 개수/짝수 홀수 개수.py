def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    
    answer = [len(a),len(b)]
    return answer