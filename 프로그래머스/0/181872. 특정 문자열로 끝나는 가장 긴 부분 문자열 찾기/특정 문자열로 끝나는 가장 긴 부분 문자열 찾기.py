def solution(myString, pat):
#     n = len(myString)
#     m = len(pat)
    
#     for i in range(n-m, -1, -1):
#         if myString[i:i+m] == pat:
#             return myString[:i+m]  
#     return ''

    return myString[:myString.rfind(pat)] + pat