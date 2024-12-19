def solution(myString, pat):
    myString = myString.replace('A','a')
    myString = myString.replace('B','b')
    myString = myString.replace('a','B')
    myString = myString.replace('b','A')
    if pat in myString:
        return 1
    else:
        return 0