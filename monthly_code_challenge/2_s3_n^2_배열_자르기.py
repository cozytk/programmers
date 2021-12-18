def solution(n, left, right):
    answer = []
    start = left // n
    left_rem = left % n
    end = right // n
    right_rem = right % n
    for i in range(n):
        if i < start:
            continue
        answer.extend([i + 1] * i + list(range(i + 1, n + 1)))
        if i == end:
            break
    return answer[left_rem:left_rem + right - left + 1]