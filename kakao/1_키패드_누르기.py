#24분

def check(n, last_L, last_R, hand):
    L_dist = abs(n - last_L) // 3 + abs(n - last_L) % 3
    R_dist = abs(n - last_R) // 3 + abs(n - last_R) % 3
    if L_dist == R_dist:
        return 'L' if hand == 'left' else 'R'
    return 'L' if L_dist < R_dist else 'R'

def solution(numbers, hand):
    answer = ''
    last_L = 10
    last_R = 12
    for i, n in enumerate(numbers):
        if n == 0:
            n = 11
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            answer += check(n, last_L, last_R, hand)
        if answer[-1] == 'L':
            last_L = n
        else:
            last_R = n
    return answer