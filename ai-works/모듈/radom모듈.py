# random() 함수는 0.0 이상 1.0 미만의 난수를 반환하는 함수입니다.
#  0.0 <= x < 1.0

import random

# print(random.random()) # 0.0 이상 1.0 미만의 난수 출력

# 1부터 10까지의 난수 출력 - randint(a, b) 함수 사용
print(random.randint(1, 10)) # 1 이상 10 이하의 난수

# 주사위 던지기
dice = random.randint(1, 6)
# print("주사위 눈:", dice)
print(f"주사위 눈: {dice}") # f-string을 사용한 출력

# 리스트에서 무작위로 요소 선택 - choice() 함수 사용
fruits = ["사과", "바나나", "딸기", "오렌지"]
print("선택된 과일:", random.choice(fruits))