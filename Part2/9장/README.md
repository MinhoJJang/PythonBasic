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

## 값으로 호출하기 vs 참조로 호출하기

값으로 호출하는 것은 call-by-value로 불리며 변수의 값을 복사한다. 참조로 호출하는 것은 call-by-reference라고 불리며 변수의 참조값이 전달된다. 이때 참조값은 해당 객체의 주소값을 뜻하며, 주소값에 있는 변수를 변경하면 기존의 변수도 당연히 값이 바뀌게 된다.

우리는 앞서, 파이썬의 객체들은 모두 주소값을 저장한다고 배웠다. 즉, `x=10`, `y="Hello"` 와 같은 식이 성립하는 이유가 변수에 데이터 타입을 저장하지 않고 데이터의 주소를 저장하는 방식이기 때문이다.

그렇다면 값을 초기화하는 것이 아니라, 초기화한 값을 호출할 때는 어떻게 될까? 파이썬에서 정수나 문자열 타입 변수는 변경이 불가능하다. 즉 값으로 호출하는 방식으로 전달된다. 이 말인 즉슨, 내부 함수에서 아무리 매개변수값을 변경해도 기존 변수에는 전혀 영향이 가지 않는다. 또한 반대로, 변경가능한 객체인 리스트는 참조값으로 전달된다. 이는 아래 코드를 살펴보면 좋다.

> CallByValue

```py
def func1(x) :
    print( "x=", x," id=",id(x))
    x=42 # 새로운 객체 생성
    print( "x=", x," id=",id(x))

y = 10
print( "y=",y," id=",id(y))
func1(y)
print( "y=",y," id=",id(y))

y= 10  id= 9801536
x= 10  id= 9801536
x= 42  id= 9802560
y= 10  id= 9801536
-> 분명히 func1에서 매개변수 x값을 42로 변경하였음에도 불구하고, 함수 외부의 y값은 변경되지 않는다.
```

> CallByReference

```py
def func2(list):
    list[0] = 99
values = [0, 1, 1, 2, 3, 5, 8]
print(values)
func2(values)
print(values)

[0, 1, 1, 2, 3, 5, 8]
[99, 1, 1, 2, 3, 5, 8]
-> 함수 내부에서 리스트 list를 변경하였는데, 함수 밖의 리스트 values가 변경된다. 즉, 이 둘은 이름만 다르고 사실상 가리키는 주소가 같다. 이를 피하기 위해서는 앞서 살펴본 깊은 복사를 하면 된다.

***

def func2(li):
    newlist = list(li)
    newlist[0] = 99
values = [0, 1, 1, 2, 3, 5, 8]
print(values)
func2(values)
print(values)

[0, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8]
```

결국에는 변경가능한 객체인지 아닌지에 따라 함수에 전달되는 값의 특성이 바뀐다. 변경가능한 객체인 리스트, 딕셔너리는 값이 Call-by-reference 방식으로 전달되고 변경불가능한 객체인 문자열, 정수, 튜플은 Call-by-value 방식으로 전달된다.

## 리스트 함축

리스트 함축은 리스트를 매우 간단하게 만들 수 있는 방법이다.

> 1. 반복문 사용하기

```py
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

> 2. 리스트 함축 사용하기

```py
s = [x**2 for x in range(5, 10, ++2)]
print(s)

[25, 49, 81]
```

확실히 리스트 함축이 간단하다! 이러한 리스트 함축은 아래 예시들에서 더 탁월한 성능을 보인다.

1. 조건이 붙는 리스트 함축

```py
M = [x for x in range(10) if x%2 == 1]
print(M)

[1, 3, 5, 7, 9]
```

2. 다양한 자료형에 대한 리스트 함축

```py
list1 = ["All", "good", "things", "must", "come", "to", "an", "end."]
items = [word[0] for word in list1]
print (items)

['A', 'g', 't', 'm', 'c', 't', 'a', 'e']
```

```py
word_list = "Doncount your chickens before they are hatched".split()
result_list = [ len(w) for w in word_list]
print(result_list)

[8, 4, 8, 6, 4, 3, 7]
```

3. 상호곱 형태의 집합

```py
colors = [ "white", "silver", "black" ]
cars = [ "bmw5", "sonata", "malibu", "sm6" ]
colored_cars = [ (x, y) for x in colors for y in cars ]
print(colored_cars)

[('white', 'bmw5'), ('white', 'sonata'), ('white', 'malibu'), ('white', 'sm6'), ('silver', 'bmw5'), ('silver', 'sonata'), ('silver', 'malibu'), ('silver', 'sm6'), ('black', 'bmw5'), ('black', 'sonata'), ('black', 'malibu'), ('black', 'sm6')]
```

## 리스트 연산들

### 최대, 최소

가장 대표적으로 최대 최소를 구하는 문제가 있을 것이다.

```py
arr = [10, 5, 3, 15, 20]
min = arr[0]

for i in range (1, len(arr)):
    if min > arr[i] :
        min = arr[i]

print(min)
```

### 탐색하기

탐색은 컴퓨터에서 매우 중요한 알고리즘으로, 여러가지 탐색 중에서 대표적으로 이분 탐색이 있다. 현재 단계에서 이분 탐색을 구현하기는 힘들기 때문에 가장 기본적인 순차 탐색만 알아보자.

```py
list1 = [ "white", "silver", "blue", "red", "blue" ]
print(list1.index ("blue"))

2
```

위 예제는 가장 기본적인 탐색 방법으로, index를 활용해 배열에서 가장 처음으로 만나는 'blue'의 위치를 찾는 방법이다. 그러나 우리가 항상 index을 사용해서 search를 할 수는 없는 법이다. 그래서 순차 탐색 코드를 간단하게 만들어 보자

```py
def linear_Search(aList, key):
    for i in range(len(aList)):
        # 리스트의 길이만큼 반복한다.
        if key == aList[i]:
            # 키가 발견되면 i를 반환하고 종료한다.
            return i
    return -1
    # 키가 발견되지 않고 반복이 종료되었으면 -1을 반환한다.
numbers = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
position = linear_Search(numbers, 30)
if position != -1:
    print("탐색 성공 위치 =", position)
else:
    print("탐색 실패 ")

탐색 성공 위치 = 2
```
