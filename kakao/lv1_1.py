def solution(s):
    eng_words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    en_dict = {i:j for i,j in zip(eng_words, range(10))}
    i = 0
    answer = 0
    while i < len(s):
        tmp = ''
        if s[i].isalpha():
            while i < len(s) and s[i].isalpha() and tmp not in en_dict.keys():
                tmp = tmp + s[i]
                i += 1
            answer = answer * 10 + en_dict[tmp]
        else:
            answer = answer * 10 + int(s[i])
            i += 1
    return answer