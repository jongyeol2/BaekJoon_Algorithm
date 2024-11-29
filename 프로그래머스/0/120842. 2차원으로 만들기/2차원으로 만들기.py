def solution(num_list, n):
    
    a = []
    
    
    for i in range(0,int(len(num_list)/n)):
        a.append(num_list[n*i:n*(i+1)])

    
    return a