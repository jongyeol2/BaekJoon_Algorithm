def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        num = sorted(array[i-1:j])[k-1]
        answer.append(num)
    return answer