def solution(polynomial):
    my_list = polynomial.split(" + ")
    my_list = ["1x" if i == "x" else i for i in my_list]
    
    x_val = 0
    num = 0
    
    for i in my_list:
        if "x" in i:
            x_val += int(i.replace("x", ""))
        else:
            num += int(i)
            
    answer = []
    if x_val:
        answer.append(f"{x_val}x" if x_val > 1 else "x")
    if num:
        answer.append(str(num))

    return " + ".join(answer)