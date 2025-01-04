def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] is True:
            X += [arr[i]]*(arr[i]*2)
        else:
            X = X[:-arr[i]]
            
    return X