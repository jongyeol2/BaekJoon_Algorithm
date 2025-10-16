def solution(elements):
    e_sum = set()
    elements_2 = (elements * 2)
    
    for i in range(len(elements)):
        s = 0
        
        for j in range(len(elements)):
            s += elements_2[i+j]
            e_sum.add(s)
            
    return len(e_sum)