def solution(myString):
    myString = myString.split('x')
        
    myString = [i for i in myString if i]
        
    myString.sort()
    return myString