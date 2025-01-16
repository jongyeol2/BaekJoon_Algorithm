def solution(num_list):
    answer = 0
    for i in num_list:
        num = 0
        while i >1:
            if i % 2 == 0:
                i = i/2
            else:
                i = (i-1)/2
            num += 1
        answer += num
    return answer