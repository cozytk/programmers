# Lv1. 숫자 문자열과 영단어 
ex) 'one2three4' -> '1234'

### 나의 코드
```python
def solution(s):
    eng_words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    en_dict = {i:j for i,j in zip(eng_words, range(10))}
    i = 0
    answer = 0
    while i < len(s):
        tmp = ''
        if s[i].isalpha():
            while i < len(s) and s[i].isalpha() and tmp not in en_dict.keys():
                tmp = tmp + s[i]
                i += 1
            answer = answer * 10 + en_dict[tmp]
        else:
            answer = answer * 10 + int(s[i])
            i += 1
    return s
```
### 개선: replace함수를 활용

```python
for key, val in en_dict.items():
    answer = answer.replace(key, value)
    return int(answer)
```


# Lv1. 신규아이디 추천

### 나의 코드
```python
    if n == '-' or n == '_' or n == '.':
```

### 개선
```python
    if n in ['-', '_', '.']:
```
---

### 나의 코드
```python
    i = 0
    tmp = ''
    while i < len(new_id):
        if new_id[i] == '.':
            while i < len(new_id) and new_id[i] == '.':
                i += 1
            tmp += '.'
        else:
            tmp += new_id[i]
            i += 1
    new_id = tmp
```

### 개선
```python
    while '..' in new_id:
        new_id.replace('..', '.')
```
---
### 나의 코드
```python
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
```

### 개선
```python
    new_id = new_id.strip('.')
```
---
### 나의 코드
```python
    if len(new_id) == 1:
        new_id = new_id * 3
    if len(new_id) == 2:
        new_id = new_id + new_id[1]
```

### 개선
```python
    while len(new_id) < 3:
        new_id += new_id[-1]
```

---

# Lv2. 거리두기 확인하기

## 걸린 시간 : 80분

### 후기
- 길이가 5X5 배열로 정해져있기 때문에 실전에서는 모든 경우의 수를 다 구해도 괜찮음
- 조건이 동적이지 않으면 for문을 사용할 것

## 개선하기

### while -> for
```python
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
```

위와 같이 0부터 4까지 인덱스를 반복하는 것이 정해져있으면, range 혹은 enumerate를 사용한 순회가 바람직

### 개선
```python
for p in places:
    result = 1
    for i, row in range(5):
        for j, col in range(5):
            if valid_place(p, i, j) == False:
                result = 0
                break
        if result == 0:
            break
    answer.append(result)
```

### 구조 단순화
```python
for p in places:
    result = 1
    for i, row in range(5):
        for j, col in range(5):
            if valid_place(p, i, j) == False:
                result = 0
                break
        if result == 0:
            break
    answer.append(result)
```

- 한 함수안에 기능을 명확히 하기 위해 의미 단위로 명확히 쪼개자
- 함수 이름도 최대한 단순히

### 개선
```python
def valid(p):
    for i in range(5):
        for j in range(5):
            . . .
            return False
    return True


for p in places:
    if valid(p) == False:
        answer.append(0)
    else:
        answer.append(1)
```


### bfs
- 너비우선탐색인줄 알았는데 깊이우선탐색을 했음
- 너비우선탐색은 queue, 깊이우선탐색은 stack, 재귀를 사용
```python
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
```

### 개선
```python
def dfs(p, i, j, start, m):
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
```

- 재귀 말고 스택으로 푸는 것도 다음번에 시도해보자