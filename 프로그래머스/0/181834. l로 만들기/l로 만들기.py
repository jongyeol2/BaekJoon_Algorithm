def solution(myString):
    for i in myString:
        if i in 'abcdefghijk':
            myString = myString.replace(i,'l')
    return myString