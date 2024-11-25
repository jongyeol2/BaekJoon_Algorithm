def solution(array):
    array.sort()
    dict_1 = {}
    
    for i in range(len(array)):
        value = array[i]
        if value in dict_1:
            dict_1[value] += 1
        else:
            dict_1[value] = 1
        
    max_cnt = max(dict_1.values())
    max_list = []
    for key,value in dict_1.items():
        if value == max_cnt:
            max_list.append(key)
    
    if len(max_list) > 1:
        return -1
    else:
        return max_list[0]
    