# 24분

def row2vec(board):
    b_len = len(board)
    result = [[0 for _ in range(b_len)] for _ in range(b_len)]
    for i in range(b_len):
        for j in range(b_len):
            result[j][i] = board[i][j]
    for r in result:
        r.reverse()
        while len(r) > 0 and r[-1] == 0:
            r.pop()
    return result
            
        

def solution(board, moves):
    board = row2vec(board)
    bucket = []
    answer = 0
    for m in moves:
        if len(board[m - 1]) > 0:
            bucket.append(board[m - 1].pop())
        if len(bucket) > 1 and bucket[-2] == bucket[-1]:
            bucket.pop()
            bucket.pop()
            answer += 2
    return answer