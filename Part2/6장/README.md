# Part 2

## 6장

## 함수

Python의 함수 역시 기타 언어들의 함수와 비슷하나, 함수 자체의 반환타입이 미리 정해지지 않았으며 파라미터값의 전달 방식에 다양한 변형을 가할 수 있다는 차이점이 있다.

기본적인 함수 원형은 아래와 같다. 함수의 반환타입도 필요 없으며 역시 파라미터의 타입도 명시할 필요가 없다.

```py
def getSum (a, b) :
    sum = 0
    for i in range(a) :
        sum += i
    return sum + b

print(getSum(10, 20))

65
```

이처럼 대부분의 함수는 리턴값으로 그 함수의 역할을 다하지만, 리턴값이 필요없는 함수도 존재한다. Python에서는 그러한 경우 `None` 이라는 특별한 값을 반환한다. None은 어떤 객체도 참조하지 않는다는 것을 의미한다.

```py
def getSum (a, b) :
    sum = 0
    for i in range(a) :
        sum += i
    # return ...

print(getSum(10, 20))

None

>>> type(None)
<class 'NoneType'>
```

Python에서는 매개변수가 기본값을 가질 수 있다. 이것을 **디폴트 인수**라고 하는데, 단순하다. 인수를 선언부에서 미리 값을 지정해놓는 것이다. 활용법은 아래 코드와 같다.

```py
def greet(name, msg="msg내용") :
    print("Hi ", name + ", " + msg)

greet("철수")
greet("영희", "인자값 넣어주기")

Hi  철수, msg내용
Hi  영희, 인자값 넣어주기
```

Python에서는 **키워드 인수** 가 있는데, 직접 매개변수 이름에다가 값을 넣는 방식이다. 이렇게하면 매개변수가 많은 함수에서도 혼란 없이 값을 대입할 수 있고 이해하기 편하다는 장점이 있다.

```py
def calc(x, y, z):
    return x*y+z

print(calc(5,2,3))
print(calc(x=5, y=2, z=3))
print(calc(x=5, z=3, y=2))

13
13
13
```
