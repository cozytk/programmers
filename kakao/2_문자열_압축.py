def solution(s):
    shortest = s
    for l in range(1, len(s) // 2 + 1):
        tmp = ''
        i = 0
        while i < len(s):
            cnt = 1
            if s[i: i+l] == s[i+l: i+l+l]:
                stk = s[i: i+l]
                while stk == s[i+l: i+l+l]:
                    cnt += 1
                    i += l
                tmp += str(cnt) + stk
                i += l
            else:
                tmp += s[i: i+l]
                i += l
        if len(tmp) < len(shortest):
            shortest = tmp
    return len(shortest)