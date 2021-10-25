def isBalanced(s):
    openingB = ["{", "(", "["]
    closingB = ["}", ")", "]"]
    brakets = []
    loc = 0
    if len(s) == 0:
        return "NO"
    while loc < len(s):
        if s[loc] in openingB:
            brakets.append(s[loc])
        elif s[loc] in closingB:
            if len(brakets) == 0:
                return "NO"
            else:
                check = brakets.pop()
            if check == "{" and s[loc] == "}" or check == "(" and s[loc] == ")" or check == "[" and s[loc] == "]":
                pass
            else:
                return "NO"
        else:
            return "NO"
        loc += 1
    if len(brakets) > 0:
        return "NO"
    else:
        return "YES"
