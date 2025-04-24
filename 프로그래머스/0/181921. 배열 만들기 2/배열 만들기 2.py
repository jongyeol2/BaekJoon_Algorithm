def solution(l, r):
    answer = []
    
    for i in range(l,r+1):
        num = [int(j) for j in str(i)]
        if set(num) | {0, 5} == {0, 5}:
            answer.append(i)
                
    return answer if answer else [-1]