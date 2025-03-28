def solution(id_pw, db):
    answer = ''
    id_dict = {user[0]: user[1] for user in db}
    
    if id_pw[0] not in id_dict:
        return "fail"
    elif id_dict[id_pw[0]] == id_pw[1]:
        return "login"
    else:
        return "wrong pw"
    

