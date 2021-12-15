# Task 
ex) 'one2three4' -> '1234'

# Solution: replace함수를 활용하자

`answer = answer.replace(key, value)`


# Task

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
