def solution(strings, n):
    answer = []
    indexed_strings = list(enumerate(strings))
    
    sorted_words = sorted(indexed_strings, key=lambda x: (x[1][n], x[1]))
    
    for i in sorted_words:
        answer.append(i[1])
    
    return answer