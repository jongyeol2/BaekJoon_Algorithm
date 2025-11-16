import re

def solution(dartResult):
    answer = 0
    regx = re.findall(r"\d+[^0-9]*", dartResult)
    double = []
    minus = []
    
    for i in range(3):
        if "*" in regx[i]:
            regx[i] = regx[i].replace("*", "")
            double.append(i)
        if "#" in regx[i]:
            regx[i] = regx[i].replace("#", "")
            minus.append(i)
        regx[i] = regx[i].replace("S", " ** 1")
        regx[i] = regx[i].replace("D", " ** 2")
        regx[i] = regx[i].replace("T", " ** 3")

    for i in double:
        if i == 0:
            regx[0] += " * 2"
        else:
            regx[i] += " * 2"
            regx[i-1] += " * 2"
    
    for i in minus:
        regx[i] += " * -1"
    
    
    for i in regx:
        answer += eval(i)
    return answer