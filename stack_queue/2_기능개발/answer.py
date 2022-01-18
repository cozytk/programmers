def solution(progresses, speeds):
    answer = []
    while progresses:
        for i, (_, s) in enumerate(zip(progresses, speeds)):
            progresses[i] += s
        if progresses[0] >= 100:
            cnt = 0
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            answer.append(cnt)
    return answer