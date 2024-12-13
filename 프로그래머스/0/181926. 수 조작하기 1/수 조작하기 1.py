def solution(n, control):
    answer = (control.count('w')*1
             + control.count('s')*-1
             + control.count('d')*10
             + control.count('a')*-10)
    return answer + n