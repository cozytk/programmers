def solution_example(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result

def solution_mine(answers):
    personA = [1, 2, 3, 4, 5]
    personB = [2, 1, 2, 3, 2, 4, 2, 5]
    personC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    result = []
    for i, answer in enumerate(answers):
        if answer == personA[i % 5]:
            cnt[0] += 1
        if answer == personB[i % 8]:
            cnt[1] += 1
        if answer == personC[i % 10]:
            cnt[2] += 1
    for i, s in enumerate(cnt):
        if s == max(cnt):
            result.append(i + 1)
    return result

print(solution_example([1,2,3,4,5]))
print(solution_mine([1,2,3,4,5]))

