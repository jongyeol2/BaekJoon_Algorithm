def solution(myString):
    answer = []
    split = myString.split('x')
    for i in split:
        answer.append(len(i))
    return answer