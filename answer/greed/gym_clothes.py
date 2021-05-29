def solution(n, lost, reserve):
    student = [0] + [1] * n + [0]
    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1
    i = 1
    while i <= n:
        if (student[i] == 0):
            if (student[i - 1] == 2):
                student[i - 1] -= 1
                student[i] += 1
            elif (student[i + 1] == 2):
                student[i + 1] -= 1
                student[i] += 1
        i += 1
    for i in student:
        if i == 0:
            n -= 1
    n += 2
    return n