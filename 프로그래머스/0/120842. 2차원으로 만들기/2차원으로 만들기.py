def solution(num_list, n):
    answer = []
    
    for i in range(int(len(num_list)/n)):
        answer.append(num_list[n*i:n*(i+1)])

    return answer