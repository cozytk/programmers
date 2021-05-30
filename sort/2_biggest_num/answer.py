# import cmp_to_key from functools
# lambda cannot make extra variable (external variable needed)
# 0 exception caution

from functools import cmp_to_key

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x,y:int(y+x) - int(x+y)))
    for n in numbers:
        answer += n
    if (numbers[0] == "0"):
        return "0"
    return answer
