def solution(ineq, eq, n, m):
    answer = 0
    
    compare_dict = {
        ">=" : n >= m,
        "<=" : n <= m,
        ">!" : n > m,
        "<!" : n < m
    }
    
    if compare_dict[ineq + eq]:
        answer = 1
    
    return answer