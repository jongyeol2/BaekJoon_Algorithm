def solution(my_string):
    answer = [0]*52
    # A65 Z90 a97 z122
    
    for i in my_string:
        if i.isupper():
            answer[ord(i)-65] += 1
        else:
            answer[ord(i)-97+26] += 1
            
    return answer