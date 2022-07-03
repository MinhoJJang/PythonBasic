# Part 1 정리

## 4장

## 조건문

Python의 조건문 역시 C나 Java 등 기타 언어의 조건문과 크게 다르지 않지만, 양식에 차이가 있다. 일단 Python에서는 괄호를 꼭 사용하지 않아도 되며, 들여쓰기로 지역을 구분하기 때문에 이를 위해 `:`, 콜론을 사용한다. 이것은 인터프리터에게 아직 전체 문장이 끝나지 않았으니 잠시 해석을 미루어달라고 요청하는 기호이다.

```py
age = 19
if age == 19 :
    print("if문 진입")
else :
    print("else문 진입")

# if문 진입
```

그리고 Python에서는 and와 or을 표현하는 기호가 다르다. 아래 예제를 보면, C나 Java에서 and연산 시 `&&` 기호를 사용했으나 Python에서는 영어 그대로 `and` 를 사용한다. or도 마찬가지이다.

```py
if age == 19 and test == 10 :
    print("and 연산자")

# and 연산자
```

또한 Python에서는 else if 문을 줄여서 `elif` 을 사용한다.

```py
if age > 20 :
    print("if문")
elif age > 10 and age <= 20 :
    print("elif문")
else :
    print("else문")

# elif문
```
