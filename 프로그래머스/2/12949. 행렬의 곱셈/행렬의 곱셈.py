def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    k = len(arr2[0])
    answer = [[0]*k for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for l in range(m):
                answer[i][j] += arr1[i][l] * arr2[l][j]
                
    return answer