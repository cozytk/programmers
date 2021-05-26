def solution(answers):
    personA = [1, 2, 3, 4, 5]
    personB = [2, 1, 2, 3, 2, 4, 2, 5]
    personC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    answer = []
    for i in enumerate(answers):
        if answers[i] == personA[i % 5]:
            cnt[0] += 1
        if answers[i] == personB[i % 8]:
            cnt[1] += 1
        if answers[i] == personC[i % 10]:
            cnt[2] += 1
    max_score = max(cnt[0], cnt[1], cnt[2])
    for i in enumerate(cnt):
        if max_score == cnt[i]:
            answer.append(i + 1)
    return answer

# can't compile(interpret?)
# TypeError: list indices must be integers or slices, not tuple
