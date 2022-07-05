# Part2

## 7장

## 참조값에 의한 인수 전달

특히 C에서 중요하게 다뤘던 내용과 일맥상통한다. Python에서도 C와 마찬가지로 `call-by-value` 와 `call-by-reference` 의 차이점이 존재한다.

함수의 파라미터로 들어가는 값은, 그 변수의 주소값이 아니라 변수의 값을 복사해서 함수로 진입한다. 따라서, 아래 예시처럼, k값은 아무리 `modify()`를 해도 `modify()` 내부에서만 값이 변경되며 변경된 값은 원래 변수 k 주소에 영향을 주지 않는다. `print((modify(k)))` 에서도 단순히 `modify(k)`의 리턴값이 `n` 이라서 값이 11이 나온 것일 뿐이고, 실제 k값은 10에서 변하지 않는다. 이것이 **call-by-value** 이다.

```py
def modify(n) :
    n += 1
    return n

k = 10
print(k)
modify(k)
print(k)
print((modify(k)))

10
10
11

***

def mod(s):
    s+="Plus"
    return s

msg = "Message"
print(msg)
mod(msg)
print(msg)
print(mod(msg))

Message
Message
MessagePlus
```

이는 숫자뿐만 아니라 문자열에도 해당된다. 즉, Python에서는 선언한 숫자나 문자열은 **변경 불가능한 객체**임을 알 수 있다. 일단 한번 해당 주소에 숫자나 문자열이 배정받고 나면, 절대 변하지 않는다는 것이다. 만약 숫자나 문자열을 바꾸는 순간 주소값도 바뀔 것이다.

```py
msg = "Hi"
print(id(msg))
msg += " Hello"
print(id(msg))

139734708060528
139734708061488
```

그렇다면 만약 변경 가능한 객체, 리스트를 전달하면 어떻게 될까?

```py
def modify(li):
    li += [100, 200]

list = [1, 2, 3, 4, 5]
print(list)
modify(list)
print(list)

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 100, 200]
```

숫자나 문자열을 넣었을 때와는 전혀 다른 결과가 나온 것을 볼 수 있다. 이처럼 리스트를 함수의 인자값으로 전달하면, 값의 복사가 일어나는 것이 아니라 리스트의 참조값이 전달된다. 즉 리스트의 주소를 직접 건드리기 때문에 리스트 원본이 변경된다.

## 지역변수와 전역변수

개념 자체는 기타 언어들과 같다. Python에 추가된 내용만 알아보자. 지역변수, 전역변수하면 흔히 나오는 예제가 바로 아래 코드이다.

```py
def sub():
    s = "바나나가 좋음!" # 지역변수
    print(s)

s = "사과가 좋음!" # 전역변수
sub()
print(s)

바나나가 좋음!
사과가 좋음!
```

즉, 전역변수 s보다 지역변수 s가 함수에서는 우선순위가 높다. 또한 지역변수와 전역변수는 아예 다른 공간이므로 같은 변수 이름이더라도 지역마다 s의 값이 다르다. 그래서 아래와 같은 코드는 오류가 발생한다.

```py
def sub():
    print(s) # 오류코드
    s = "바나나가 좋음!"
    print(s)

s = "사과가 좋음!"
sub()
print(s)

UnboundLocalError: local variable 's' referenced before assignment
```

s를 지역변수를 써야 하나? 전역변수를 써야 하나? 정하지 못해 오류가 발생한다. 그러면 어떤 변수를 써야 할지 정해주면 되겠네? 그래서 Python에서는 `global`이라는 키워드를 사용한다.

```py
def sub():
    global s # 함수 안에서 전역 변수 s를 사용하겠다 라는 의미
    print(s)
    s = "바나나가 좋음!" # 전역변수 값 변경
    print(s)
s = "사과가 좋음!!"
sub()
print(s)

사과가 좋음!!
바나나가 좋음!
바나나가 좋음!
```

아래 문제를 쉽게 풀었다면 개념이 확립된 것이다.

```py
def sub(x, y):
    # 함수의 매개 변수도 지역 변수의 일종이다.
    global a
    #함수 안에서 전역 변수 a를 사용하겠다는 의미.
    a=7
    x, y = y, x
    b=3
    print(a, b, x, y) # 7 3 4 3

a, b, x, y = 1, 2, 3, 4
sub(x, y)
print(a, b, x, y) # 7 2 3 4
```

## 여러 개의 값 반환하기

놀랍게도 Python에서는 리턴값 수에 제한이 없다! 그래서 아래와 같은 코드가 가능하다. 이는 추후에 tuple 을 다루게 되면 자세히 알아보도록 하자.

```py
def sub():
    return 1, 2, 3
a, b, c = sub()
print(a, b, c)

1 2 3
```

## 무명함수 (람다식)

람다식은 함수를 축약한 형태와 비슷하다. 주로 단순 계산을 위해 사용된다. 예를 들어 아래 예제처럼, 어떤 수를 빠르게 2를 곱하거나 나눌 때 사용되는 shift 연산자를 함수화하여 사용할 수 있다.

```py
left_shift = lambda x : x>>1

print(bin(left_shift(0b1100100)))

0b110010
```

혹은 리스트에다 람다식을 넣을 수도 있다. 예를 들어 아래와 같이 효율적인 코드로 계산기를 만들 수 있다.

```py
calculate = [lambda x,y : x+y,
             lambda x,y : x-y,
             lambda x,y : x*y,
             lambda x,y : x/y]

operator = ['+', '-', '*', '/']

x = int(input("첫번째 수를 입력하세요 : "))
op = input("연산자를 입력하세요 : ")
y = int(input("두번째 수를 입력하세요 : "))

print(calculate[operator.index(op)](x,y))
```

## 모듈

모듈은 자바의 클래스와 비슷한 개념이라고 생각된다. 자바에서 기타 클래스들을 import 하듯이, \*.py 파일들을 가져와서 사용할 수 있다.

```py
# 피보나치 수열 모듈 import fibo
def fib(n): # 피보나치 수열을 화면에 출력한다.
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

***
# 방법 1
import fibo

fibo.fib(1000)

1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print(fibo.__name__)

'fibo’

***
# 방법 2
from fibo import *
fib(500)

1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
