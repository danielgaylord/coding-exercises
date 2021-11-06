def one_away(s1, s2):
    p1, p2 = 0, 0
    edit = False
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif not edit:
            if p1 + 1 < len(s1) and s1[p1 + 1] == s2[p2]:
                p1 += 1
                edit = True
            elif p2 + 1 < len(s2) and s1[p1] == s2[p2 + 1]:
                p2 += 1
                edit = True
            elif p1 + 1 < len(s1) and p2 + 1 < len(s2) and s1[p1 + 1] == s2[p2 + 1]:
                p1 += 1
                p2 += 1
                edit = True
            else:
                return False
        else:
            return False
    if p1 == p2 or (abs(p1 - p2) == 1 and not edit):
        return True
    else:
        return False 