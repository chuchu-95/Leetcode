def judgeCircle(moves):
    org = [0, 0]
    r = moves.count("R")
    l = moves.count("L")
    u = moves.count("U")
    d = moves.count("D")
    org_re = [r+(-1)*l, u+(-1)*d]
    return True if org == org_re else False


print(judgeCircle("LL"))

