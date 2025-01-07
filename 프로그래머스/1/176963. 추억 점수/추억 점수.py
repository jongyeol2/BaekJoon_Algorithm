def solution(name, yearning, photo):
    answer = []
    dict = {}
    
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for i in photo:
        num = 0
        for j in i:
            if j in dict.keys():
                num += dict[j]
        answer.append(num)
    
    return answer