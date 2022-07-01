# Part 1 정리

## 3장

## 자료형

Python의 자료형은 `정수, 실수, 문자열` 3가지가 있다. 정말 간단하다! 각각 int, float, str에 해당하며, type()로 타입을 체크할 수 있다. 그리고 당연하지만 True, False를 체크하는 boolean 형은 기본이다.

```py
>>> type(3.2)
<class 'float'>
>>> type('Hello')
<class 'str'>
>>> type(17)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

---

또한, 파이썬의 변수 선언 시 자료형을 딱히 미리 정해줄 필요가 없다. 따라서, 매우 자유롭게 자료형을 변경할 수 있다. 이는 C, Java에서 `int x = 10;` 이런 식으로 변수를 생성하고 초기화하던 것과는 차원이 다른 편리함이다.

```py
>>> x = 3.2
>>> x
3.2
>>> x = 'hello'
>>> x
'hello'
>>> x = "hello"
>>> x
'hello'
```

다만 주의해야 할 것은 `문자열 "10" 과 숫자 10` 이다.

```py
>>> x = "10"
>>> y = 10
>>> x+y
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
# Java의 경우 문자열과 숫자를 연산하면 숫자가 자동으로 문자열로 변경되어 적용되었으나, Python에서는 필히 str() 혹은 int() 을 통해 타입을 통일시킨 후 연산해야한다.
>>> x
'10'
>>> y
10
>>> x+str(y)
'1010'
>>> int(x)+y
20
```

또한 값을 비교하는 것에도 당연히 차이가 있다. 정수값과 실수값을 비교하는 것은 값에 차이가 없다면 True가 나오지만, 문자열과 숫자는 결코 비교할 수 없다.

```py
>>> x = 10
>>> y = '10'
>>> z = 10.000
>>> x == z
True
>>> z == y
False
>>> x == y
False
```

## 문자열

Python의 문자열은 생성 규정이 까다롭지 않다. 작은 따옴표든, 큰 따옴표든 같은 따옴표로만 묶으면 문자열로 인식한다. 즉, 위 규칙을 따르지 않으면 당연히 오류가 발생한다.

```py
>>> greeting = "Hello'
File "<stdin>", line 1
greeting = "Hello'
^
SyntaxError: EOL while scanning string literal
>>> greeting = 'hello
File "<stdin>", line 1
greeting = 'hello
^
SyntaxError: EOL while scanning string literal
```

여기서 EOL은 End Of Line의 줄임말이다. 큰 따옴표가 있을 것으로 기대하였는데 줄의 끝을 만날 때까지 발견하지 못했다는 의미이다.

---

Python의 문자열은 왜 두가지 따옴표 모두를 허용할까? 바로 아래와 같이 문장 안에 따옴표가 들어갈 경우를 생각해서이다.

```py
>>> str = "he said, "Hi" "
File "<stdin>", line 1
str = "he said, "Hi" "
^
SyntaxError: invalid syntax

>>> str = "he said, 'Hi' "
>>> str
"he said, 'Hi' "
```

또한, 파이썬 역시 이스케이프 문자가 존재하며 각각의 이용 예시는 아래와 같다.

```py
# \' : 작은따옴표를 표시하기 위해 사용한다. 큰따옴표도 똑같다.
>>> msg = 'doesn't'
File "<stdin>", line 1
msg = 'doesn't'
^
SyntaxError: invalid syntax
>>> msg = 'doesn\'t'
>>> print(msg)
doesn't

# /t : tab , /n : 줄바꿈
>>> print("c:\temp\name")
c:      emp
ame
# r : r을 문자열 앞에 붙이면 특수문자로 해석하지 않는다
>>> print(r"c:\temp\name")
c:\temp\name

# \\ : 백슬래시 \
>>> print(r"c:\\temp\\name")
c:\\temp\\name
>>> print("c:\\temp\\name")
c:\temp\name
```

---

Python의 특이한 점은 문자열에 \* 연산을 할 수 있다는 것이다. 그래서 반복되는 문자열을 만들기 매우 쉽다.

```py
>>> line = "=" * 10
>>> print(line)
==========
>>> msg = "iteration"
>>> print(msg*3)
iterationiterationiteration
```

또한 문자열을 출력하려면 `%s` 를 사용한다.

```py
>>> price = 1000
>>> print("상품의 가격은 %s원 입니다." %price)
상품의 가격은 1000원 입니다.
>>> msg = "현재 시간은 %s입니다."
>>> time = "22:37"
>>> print(msg % time)
현재 시간은 22:37입니다.
>>> print(msg, time)
현재 시간은 %s입니다. 22:37
>>> print(msg+time)
현재 시간은 %s입니다.22:37
>>> msg = "오늘은 %s월 %s일 입니다."
>>> print(msg % (7,1))
오늘은 7월 1일 입니다.
```

## 인덱싱 (Indexing)

지금까지 배운 문자열은 사실상 Python의 배열이다. 다만 다른 언어와 약간 차이가 존재한다. 원래라면, 맨 첫번째 글자는 항상 0번째 index 이지만 Python은 인덱스가 **음수** 가 될 수도 있다. 이때 음수 인덱스는 -1부터 시작하는데, -1이 가장 맨 뒤 글자이다.

```py
>>> word = 'Python'
>>> word[0]
'P'
>>> word
'Python'
>>> word[4]
'o'
# Python에서 한번 작성된 문자열은 변경이 불가하다.
>>> word[0] = 'C'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## 리스트(List)

여러개의 값을 모아서 하나의 변수에 저장할 수 있다. 마치 C의 `char[][]` 2차원 배열처럼, Python은 List를 간단하게 구현할 수 있다.

```py
>>> shopping_list = ['milk', 'eggs', 'cheese', 'butter', 'cream']
>>> print(shopping_list)
['milk', 'eggs', 'cheese', 'butter', 'cream']
# 리스트는 각각의 내용에 대해 index를 갖고 있다.
>>> print(shopping_list[2])
cheese
# 항목 변경이 가능하다.
>>> shopping_list[2] = 'apple'
>>> print(shopping_list)
['milk', 'eggs', 'apple', 'butter', 'cream']
```

## Python Tutor

[pythonTutor](https://pythontutor.com/visualize.html#mode=edit)

Python 코드를 시각화하여 어떤 식으로 작동되는지 보여주는 사이트이다. 잘 쓰면 좋을듯하다.
