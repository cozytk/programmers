# Lv2. n^2 배열 자르기
## 후기
- 2중 for문으로 순회시 $log(n^2)$의 시간 복잡도. input이 $10^7$ 범위이기 때문에 시간을 줄여야함

### 나의 코드
```python
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
```

- for문에 추가할때 left와 right 사이에 존재하지 않는 것은 애초에 list에 extend하지 않는 식으로 속도 줄임
- list의 extend가 $log(kn)$ 이라고 생각해서 deque로 개선해보려고 했는데 오히려 더 느려졌었음

### 아이디어
```python
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer
```
- max(i//n, i%n) + 1 이라는 아이디어를 떠올리면 간단히 풀 수 있음