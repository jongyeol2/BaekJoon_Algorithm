def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
    
    return answer

#     connect_arr = []
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         for j in range(i + 1):
#             matrix[i][j] = i + 1
#             matrix[j][i] = i + 1
    
#     for i in range(n):
#         connect_arr += matrix[i]
    
#     answer = connect_arr[left:right + 1]
    
#     return answer