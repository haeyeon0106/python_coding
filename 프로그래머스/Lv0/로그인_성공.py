def solution(id_pw, db):
    id_check,pw_check = 0,0
    for id,pw in db:
        if id_pw[0] != id:
            continue
        elif id_pw[0] == id:
            if id_pw[1] != pw:
                return "wrong pw"
            elif id_pw[1] == pw:
                return "login"
    return "fail"