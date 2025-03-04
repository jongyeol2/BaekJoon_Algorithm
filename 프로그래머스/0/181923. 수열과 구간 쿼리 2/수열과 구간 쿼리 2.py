def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        min_list = []
        for i in range(s,e+1):
            if arr[i] > k:
                min_list.append(arr[i])
        if not min_list:
            min_list.append(-1)
        answer.append(min(min_list))
    return answer