def solution(rsp):
    rsp = rsp.replace('2','zero')
    rsp = rsp.replace('0','five')
    rsp = rsp.replace('5','two')
    rsp = rsp.replace('two','2')
    rsp = rsp.replace('zero','0')
    rsp = rsp.replace('five','5')
    return rsp
    
    # answer = ''
    # for i in rsp:
    #     if i == '2':
    #         answer += '0'
    #     elif i == '0':
    #         answer += '5'
    #     elif i == '5':
    #         answer += '2'
    # return answer