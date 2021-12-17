# 맨해튼 거리 |r1 - r2| + |c1 - c2|
# 맨해튼 거리 > 2 or 사이 파티션
# 자리 P, 빈 테이블 0, 파티션 X

# bfs dfs?

# 1. P가 있을때마다 유클리드 거리를 체크해봄
 
def bfs(p, i, j, start, m):
    if (i < 0 or i > 4 or j < 0 or j > 4 or
        p[i][j] == 'X' or
        abs(start[0] - i) + abs(start[1] - j) > 2 or
        m[i][j] == 1):
        return True
    if ((i, j) != start and
        p[i][j] == 'P' and
        abs(start[0] - i) + abs(start[1] - j) <= 2):
        return False
    m[i][j] = 1
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    for idx in range(4):
        if bfs(p, i + dy[idx], j + dx[idx], start, m) == False:
            return False
    return True

def valid_place(p, i, j):
    m = [[0 for _ in range(5)] for _ in range(5)]
    if p[i][j] != 'P':
        return True
    elif bfs(p, i, j, (i, j), m):
        return True
    else:
        return False

def solution(places):
    answer = []

    for p in places:
        i, j = 0, 0
        answered = 0
        while i < 5:
            j = 0
            while j < 5:
                if valid_place(p, i, j) == False:
                    answer.append(0)
                    answered = 1
                    break
                j += 1
            if answered == 1:
                    break
            i += 1 
        if answered == 0:
            answer.append(1)
            
    return answer