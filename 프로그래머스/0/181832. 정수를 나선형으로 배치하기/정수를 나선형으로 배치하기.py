def solution(n):
    # 0 으로 이루어진 n*n배열 
    answer = []
    for _ in range(n):
        answer.append([0]*n)
        
    num = 1
    
    arr_x_index = 0              # 왼쪽상단[0][0] 좌표 0,0 이라고 가정하면
    arr_y_index = 0
    
    way = 'right'                # 진행방향설정 (시작이 오른쪽으로 가니까)
    
    while n**2 >= num:
        answer[arr_y_index][arr_x_index] = num
        num += 1
        
        
        if way == 'right':                                                      # 오른쪽으로 진행중일때
            if arr_x_index + 1 == n or answer[arr_y_index][arr_x_index+1] != 0: # 더이상 오른쪽 갈때없거나 이미 채운거라 0 이아니면 
                arr_y_index += 1                                                # 밑으로 한칸간다 (y+1)
                way = 'down'                                                    # 밑으로진행중으로 교체
            else:
                arr_x_index += 1                                                # 갈수있으니까 오른쪽 한칸이동
                
        elif way == 'down':                                                     # 밑으로 진행중일때
            if arr_y_index + 1 == n or answer[arr_y_index+1][arr_x_index] != 0: # 밑으로 더못가거나 이미 채운거라 0 아니면
                arr_x_index -= 1                                                # 한칸 왼쪽으로 감 (x-1)
                way = 'left'                                                    # 왼쪽진행중으로 교체
            else:
                arr_y_index += 1                                                # 갈수있으니까 밑으로 한칸이동 (y+1)
                
        elif way == 'left':                                                     # 왼쪽 진행중일때
            if arr_x_index - 1 < 0 or answer[arr_y_index][arr_x_index-1] != 0:  # 더왼쪽못가거나 이미 채워서 0이 아니면
                arr_y_index -= 1                                                # 위로 한칸 이동 (y-1)
                way = 'up'                                                      # 위로진행으로 교체
            else:
                arr_x_index -= 1                                                # 갈수있으니 왼쪽한칸이동 (x-1)
                
        elif way == 'up':                                                       # 위로진행중일때
            if arr_y_index -1 <0 or answer[arr_y_index-1][arr_x_index] != 0:    # 위로 더 못가고 이미 채워서 0이아니면
                arr_x_index += 1                                                # 오른쪽으로 이동 (x +1)
                way = 'right'                                                   # 오른쪽진행으로 교체
            else:
                arr_y_index -= 1                                                # 갈수있으니 위로한칸이동 (y-1)
    return answer          
            
#    [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
#     [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
    
    
#     answer = [[i for i in range(1, n+1)] for _ in range(n)]
    
#     #오른쪽끝에서 밑으로 
#     for i in range(n-1):
#         answer[i+1][-1] = answer[i][-1]+1
#     # 오른쪽밑에서 왼쪽밑으로
#     for i in range(1, n):
#         answer[-1][-i-1] = answer[-1][-i]+1

#     num = answer[-1][0] + 1
    
#     # 왼쪽밑에서 왼쪽위로
#     for i in range(n-2, 0, -1):
#         answer[i][0] = num
#         num += 1
#     # 왼쪽위에서 오른쪽위로
#     for i in range(1, n-1):
#         answer[1][i] = num
#         num += 1

    