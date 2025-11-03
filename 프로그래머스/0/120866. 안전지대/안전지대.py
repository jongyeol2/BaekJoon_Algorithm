def solution(board):
    n = len(board)
    danger = [[0] * n for _ in range(n)]
    direction = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in direction:
                    nx, ny = i + dx, j+ dy
                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1
    
    safe_cnt = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_cnt += 1
    
    
    return safe_cnt