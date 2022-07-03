# Part 1 정리

## 5장

## 반복문

반복문에는 for, while문이 있다. 이때 Python만의 for과 while문 양식을 살펴보자...

### for

역시 Python은 간단하다. 기타 언어에서는 `for(int x = 0; x<10; x++)` 이런 양식이었다면, Python은 `range(5)`와 같은 range 함수를 사용해 반복횟수를 정한다. 혹은 index가 존재하는 list를 사용할 수도 있다. 활용 방법은 아래 예시를 참고하자.

```py
for x in range(5) :
    print(x)

0
1
2
3
4

for name in ["a", "b", "c", "d"] :
    print(name)

word = "abcd"
for name in word :
    print(name, end=" ")

a
b
c
d
a b c d

sum = 0
for x in range(10) :
    sum = sum + x
print(sum)

45

# 0부터 1씩 더하면서 값을 반환하되, 10 미만까지만 반환한다.
sum = 0
for x in range(5, 10) :
    sum = sum + x
print(sum)

35

# 1부터 2씩 더하면서 값을 반환하고, 10보다는 작은 정수를 반환한다.
sum = 0
for x in range(1, 10, 2) :
    sum = sum + x
print(sum)

25
```

### while

while문은 if문과 비슷하다. 다만, while의 특성상 조건문을 적절하게 조절할 수 있는 값이 필요할 수 있는데 그것을 보초값이라고 한다. 사실 특별한 것은 아니고, 상식적으로 말이 안되는 값이 들어오는 순간 반복문을 종료하는 방식이다. 예를 들어 점수를 입력하여 평균을 구하는 프로그램에 음수값을 넣으면 그것은 점수가 될 수 없는 값이므로 그 이후로부터는 더 이상 값을 받지 않는 방식이다.

```py
n = 0
sum = 0
score = 0
print("종료하려면 음수를 입력하시오")
# grade가 0이상이면 반복
# 성적을 입력받아서 합계를 구하고 학생 수를 센다.
while score >= 0 :
    score = int(input("성적을 입력하시오: "))
    if score > 0:
        sum = sum + score
        n = n + 1

# 평균을 계산하고 화면에 출력한다.
if n > 0 :
    average = sum / n
print("성적의 평균은 %f입니다." % average)
```

### 문자열 처리하기

간단한 예시로, 입력으로 들어온 문자열의 모음 개수를 세서 반환하는 함수를 만들어보자.

```py
original = input('문자열을 입력하시오: ')
word = original.lower()
# 입력 받은 문자열을 소문자로 변경한다.
vowels = 0
consonants = 0
if len(original) > 0 and original.isalpha(): # 문자열의 길이가 0초과이고, 알파벳이라면….
    for char in word:
    # 각 문자에 대한 반복을 실행
        if char in 'aeiou':
        # 모음이라면…
            vowels = vowels + 1
            # vowels변수에 1을 증가한다.
        else:
        # 모음이 아니라면…
            consonants = consonants + 1
            # consonants변수에 1을 증가한다.
print("모음의 개수", vowels)
print("자음의 개수", consonants)
```
