# 리스트 복사하기
# 얕은 복사(shallow copy) : 주소값을 공유하는 개념. 원본 리스트에 영향을 미치는 복사 방법으로 사실 복사라고 말하기 어렵다. 


scores = [10,20,30,40,50]
refer = scores
print("scores의 주소값: ", id(scores))
print("refer의 주소값: ", id(refer))

# 사실상 scores와 refer은 같은 배열을 가리키는 다른 이름일 뿐이다. 

refer[0] = 100
refer.append(-70)
refer.insert(1, -100)
print(scores)

# 즉 refer을 변경하였는데 scores가 바뀌는 현상이 발생하게 된다. 