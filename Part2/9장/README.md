# Part 2

# 9장

## 리스트 복사하기

리스트는 예전에 한번 언급했듯이, 리스트 변수는 리스트 객체를 직접 저장하고 있지 않다. 즉, 리스트 변수는, 리스트 자체가 아니라, 리스트의 주소값이다. 따라서 아래와 같은 상황이 가능하다.

```py3
>>> score = [ 1,2,3]
>>> score
[1, 2, 3]
>>> value = score
>>> value
[1, 2, 3]
>>> value[1] = 200
>>> value
[1, 200, 3]
>>> score
[1, 200, 3]
>>> score is value
True
```

분명 value가 score을 복사한 리스트인데, value의 값을 변경하자 score의 값 역시 변경된다. 이를 **얕은 복사**라고 하며, 이는 단순히 리스트를 지칭하는 변수 이름이 하나 늘어날 뿐 각 리스트 변수가 가리키는 리스트 객체 주소는 동일하다. 따라서 마지막 코드 `score is value` 에서 `True` 가 나오게 된다.

그렇다면 깊은 복사는 어떻게 할까? 세 가지 방법으로 할 수 있다.

```py3
# 1. list() 사용
>>> value = list(score)
>>> value
[1, 200, 3]
>>> value[1] = 100
>>> value
[1, 100, 3]
>>> score
[1, 200, 3]

# 2. deepcopy 사용
>>> from copy import deepcopy
>>> deepcopyScore = deepcopy(score)
>>> deepcopyScore
[1, 200, 3]
>>> deepcopyScore[1] = 2
>>> deepcopyScore
[1, 2, 3]
>>> score
[1, 200, 3]

# 3. [:] 사용
>>> score = [1,2,3]
>>> value = score[:]
>>> value[2] = 300
>>> score
[1, 2, 3]
>>> value
[1, 2, 300]
>>> value1 = score[0:1]
>>> value1
[1]
>>> value2 = score[1:3]
>>> value2
[2, 3]
```
