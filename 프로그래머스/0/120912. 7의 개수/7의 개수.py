def solution(array):
    answer = 0
    for i in array:
        num = str(i).count("7")
        answer += num
    return answer