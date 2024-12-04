def solution(s):
    answer = True
    
    # 열고 (
    # 닫고 )
    # 닫고로 시작하거나 열고로 끝나면 false     
    # n번 열었으면 n번 닫기전까지 열면 false   
    # n번 열고 (n번이상) 닫으면 false         
    # 나머지 true 
    
    # 주석 그대로 코드짜보면
    
    # 조건1
    # if s[0] == ')' or s[-1] == '(':
    #     answer = False
    
    num = 0
    
    # 조건2,3 -> 순회하면서 열면 +1 닫으면 -1 
    for i in s:
        if i == '(':
            num += 1
        elif i == ')':
            num -= 1
        
        if num < 0:
            answer = False
            
    # 테스트17 실패 -> n번 열어놓고 n번 안닫은경우 처리안해놈 ex) (((()) -> 이런거 False 안나옴
    # n번 열었으면 무조건 n번 닫아야함
    if num != 0:
        answer = False
    
    

    return answer