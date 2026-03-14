# 리스트 - 여러 개의 값을 순서대로 저장할 수 있는 자료형
# 리스트는 대괄호[] 사용
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers)) # <class 'list'>

# 리스트의 개수 - len() 함수
print(len(numbers))

# 리스트의 요소에 접근(검색) - 인덱스 사용
print(numbers[0]) #1
print(numbers[4]) #5
print(numbers[-1]) #5  # 마지막 요소 - 인덱스는 -1부터 시작
print(numbers[-2]) #4  # 뒤에서 두 번째 요소

# 문자형 리스트
carts = ["커피", "라면", "쌀", "토마토"]

# 리스트의 요소 변경(라면 -> 초코파이)
carts[1] = "초코파이"
print(carts)

# '토마토' 검색해서 출력해 주세요
print(carts[3]) # 토마토

# 리스트의 요소 추가 - append() 메서드
carts.append("사과")
print(carts)

# 리스트의 요소 삭제 - del 키워드
# del carts[2]
carts.remove("쌀") # remove() 삭제 함수
print(carts)