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
