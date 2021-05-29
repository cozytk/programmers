# Available enumerate to range
# collections class, counter method, list(answer.key())[0] grammer
# hash method

# Mine

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, c in enumerate(completion):
        if (c != participant[i]):
            return participant[i]
    return participant[-1]

# example1

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# example2

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
