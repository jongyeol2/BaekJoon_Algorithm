def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    
    for i in arr1:
        bin_i = bin(i)[2:].zfill(n)
        bin_arr1.append(bin_i)
    for i in arr2:
        bin_i = bin(i)[2:].zfill(n)
        bin_arr2.append(bin_i)
        
    for b1, b2 in zip(bin_arr1, bin_arr2):
        string = ""
        for i, j in zip(b1, b2):
            if int(i)+int(j) > 0:
                string += "#"
            else:
                string += " "
        answer.append(string)
        
    return answer