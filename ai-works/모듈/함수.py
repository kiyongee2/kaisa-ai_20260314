# 함수 - 특정 작업을 수행하는 코드 묶음(작은 프로그램)
# 함수 정의
def greet():
    print("안녕하세요!")

# 매개변수(인자) - 함수에 전달되는 값
def greet_name(name):
    print(f"안녕하세요, {name}님!")
    
# 함수 호출
# greet()
# greet_name("홍길동")
# greet_name("우영우")

# 반환값 - 함수가 결과를 반환하는 경우
# 매개변수가 없는 경우
def message():
    return "Good Luck!"

msg = message() # 호출
print(msg) # Good Luck!

# 매개변수가 1개 있는 경우
def square(x):
    return x * x

result = square(5) # 호출
print(result) # 25

# 매개변수가 2개 있는 경우
def add(a, b):
    return a + b

sum_result = add(3, 4) # 호출
print(sum_result) # 7