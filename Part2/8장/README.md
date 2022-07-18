# Part2

## 8장

## 리스트

배열을 생각하면 된다. Python에서 리스트는 배열이나 다름없지만, 배열보다 훨씬 편리한 점을 가지고 있다.

리스트를 생성하는 법은 간단하다.

```py
scores = [ 32, 56, 64, 72, 12, 37, 98, 77, 59, 69]
```

이렇게 초기값이 있다면 위와 같은 방식으로 만들어주면 되지만, 공백 리스트를 생성한 후 값을 하나씩 넣고 싶을 경우에는 아래와 같이 만든다. `append` 함수를 사용하여, 리스트에 값을 추가할 수 있다.

```py
scores = []
for i in range(10):
    scores.append(int(input("성적을 입력하시오:")))
print(scores)
```

혹은 리스트 클래스를 사용하여 만들어 줄 수도 있다.

```py
list1 = list()
list2 = list("Hello")
list3 = list(range(0, 5))

print(list1)
print(list2)
print(list3)

[]
['H', 'e', 'l', 'l', 'o']
[0, 1, 2, 3, 4]
```

---

Python에서는 리스트가 객체가 나열된 형태이고, 그 객체는 자료형이 달라도 상관없다. 따라서 하나의 리스트에 int, float, str, 심지어 또 다른 리스트 등 어떤 데이터 타입이 들어와도 문제없다.

```py
myList = ["apple", [8, 4, 5]]
print(myList[0])
print(myList[1])

apple
[8, 4, 5]

list3 = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]] # 내장 리스트

print(list3[1][0])
print(list3[1][1])
print(list3[1][1][0])
print(list3[1][1][1][2])

bbb
['ccc', ['ddd', 'eee', 45]]
ccc
45
```

## 시퀀스 자료형

시퀀스, sequence는 문자 그대로 순서 라는 의미를 갖고 있다. 지금까지 알아봤던 문자열, 리스트가 바로 시퀀스 자료형에 속하며 이들의 특징은 **순서를 가진 요소들의 집합**이라는 것이다. 즉, 요소들에 index가 존재한다.

지금 우리가 배우고 있는 리스트에서 사용가능한 연산과 함수에는 여러가지가 있는데, 하나씩 알아보자.

| 함수&연산자 | 설명                      | 예시                        | 결과                      |
| ----------- | ------------------------- | --------------------------- | ------------------------- |
| len()       | 길이계산                  | len([1,2,3])                | 3                         |
| +           | 2개의 시퀀스 연결         | [1,2]+[3,4,5]               | [1,2,3,4,5]               |
| \*          | 반복                      | ['Hi!'] \* 3                | ['Hi!','Hi!','Hi!']       |
| in          | 소속                      | 3 in [1,2,3]                | True                      |
| not in      | 소속하지 않음             | 5 not in [1,2,3]            | True                      |
| []          | 인덱스                    | myList[1]                   | myList의 1번째 index 요소 |
| min()       | 시퀀스에서 가장 작은 요소 | min([1,2,3])                | 1                         |
| max()       | 시퀀스에서 가장 큰 요소   | max([1,2,3])                | 3                         |
| for         | 반복                      | for x in [1,2,3] : print(x) | 1 2 3                     |

---

Python의 리스트는 슬라이싱도 기본제공한다. 가볍게 코드만 보고 넘어가자

```py
squares = [0,1,4,9,16,25]
squares[3:6]
# [9,16,25]
# 3번째 index부터, 6번째 index 전까지
squares[:3]
# [0,1,4] == squares[0:3]
# 0번째 index부터, 3번째 index 전까지
```

또한 리스트는 문자열과는 다르게, 변경도 가능하고 추가 및 삭제가 가능하다. 즉, CRUD가 가능하다.

## 리스트의 기초 연산들

### 리스트 합병 및 반복

리스트를 합칠때는 `+`, 반복할때는 `*` 를 사용하면 된다.

### 리스트의 길이

`len()` 연산을 하면 된다.

### 요소 추가하기

`append()`를 사용한다.

### 요소 삽입하기

`append()` 메소드는 리스트 끝에 새로운 요소를 추가하지만, 때로는 기존 리스트의 특정 위치에 추가하기를 원할 수도 있다. 이런 경우 아래와 같이 `insert()` 를 사용할 수 있다.

```py
shopping_list = ["두부", "양배추", "딸기"]
shopping_list.insert(1, "생수")
print(shopping_list)
['두부', '생수', '양배추', '딸기']
```

### 요소 찾기

Python에서는 리스트에 어떤 요소가 있는지 찾을 수 있는 기본 내장함수가 존재한다.

```py
heroes = [ "스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨" ]
if "배트맨" in heroes :
    print("배트맨은 영웅입니다. ")
# 배트맨은 영웅입니다
```

`in` 연산자는 요소의 정보를 알고 있을 경우 해당 리스트 안에 요소값이 존재하는지 찾는 용도이다. 그렇다면 해당 요소값이 존재함과 동시에 몇 번째에 위치했는지 알아내려면? `index()`를 사용한다.

```py
heroes [ "스파이더맨", "슈퍼맨", "헐크", "아이언맨", "배트맨" ]
index = heroes.index ("슈퍼맨")
# 1
```

이때 index() 는 리스트에 없는 항목을 찾을 경우 오류가 발생한다. 따라서 먼저 리스트에 존재하는지 파악한 후 index를 찾으면 더 좋은 코드가 될 것이다.

```py
heroes = [ "스파이더맨", "슈퍼맨", '헐크", "아이언맨", "배트맨" ]
if "슈퍼맨" in heroes :
    index = heroes.index ("슈퍼맨")
```

### 리스트 일치 검사

비교연산자 `==, !=, >, <`를 사용해 2개의 리스트를 비교할 수 있다. 리스트를 비교하기 위해서는 당연히 리스트 내부의 자료형이 일치해야 한다. 리스트를 비교하는 과정은 or 연산 `||` 과 유사한데, 첫번째 요소부터 차례대로 검사하며 검사 도중 주어진 연산자를 만족하지 않는 요소가 나오는 순간 즉시 False를 리턴한다.

```py
>>> list1 = [1,2,3]
>>> list2 = [1,2]
>>> list1 > list2
True
>>> list1 == list2
False
>>> list1 >= list2
True
>>> list1 != list2
True
>>> list1 < list2
False
>>> list2.append(3)
>>> list1 == list2
True
>>> list1 <= list2
True
```

### 리스트 정렬하기

리스트를 정렬하는 데에는 두가지 방법이 존재한다.

1. 리스트 객체의 `sort()` 사용
2. `sorted()` 내장함수 사용

뭐가 다르냐? `sort()`는 in-place sorting이다. 즉 원본 리스트가 변경된다. 반대로 `sorted()` 는 in-place sorting이 아니다. 즉 기존 리스트를 그대로 놔두고, 새로이 정렬된 리스트를 반환한다.

```py
>>> li = [3,2,1,5,4]
>>> li.sort()
>>> li
[1, 2, 3, 4, 5]
>>> li = [2,3,1,5,4]
>>> new_li = sorted(li)
>>> new_li
[1, 2, 3, 4, 5]
>>>
```

정렬 기능을 좀 더 활용하면 아래와 같이 문자열을 문자로 쪼개 정렬할 수도 있다.

```py
>>> li = sorted("A picture is worth a thousand words.".split(), key=str. lower)
>>> li
['A', 'a', 'is', 'picture', 'thousand', 'words.', 'worth']
```

또한 sort와 sorted는 모두 bool형의 reverse 매개변수를 갖는다. 즉, `reverse = True` 일경우 역순 정렬이 가능하다.

```py
>>> li = sorted([5, 2, 3, 1, 4], reverse=True)
>>> li
[5, 4, 3, 2, 1]
```

### 문자열을 리스트로

`split()` 을 사용하면 된다. 이때 split 내부 파라미터에 어떤 값을 기준으로 나눌 것인지 알려주면 된다.

```py
>>> statement = "Where there is a will, there is a way"
>>> statement.split()
['Where', 'there', 'is', 'a', 'will,', 'there', 'is', 'a', 'way']
>>> statement.split(",")
['Where there is a will', ' there is a way']
```
