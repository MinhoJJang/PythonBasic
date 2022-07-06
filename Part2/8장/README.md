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
