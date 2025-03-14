bin(int("1234"))
def solution(s):
    answer = []
    cnt = 0
    zero = 0
    
    while s != "1":
        zero += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1

        
    answer.append(cnt)
    answer.append(zero)
        
    return answer