def solution(i, j, k):
    string = ""
    for a in range(i,j+1):
        string += str(a)
    return string.count(str(k))