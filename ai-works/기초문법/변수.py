# 변수 - 데이터를 저장하기 위해 이름을 붙인 공간
# 변수는 값을 변경할 수 있음
# 상수 - 변하지 않는 값

print(4 + 5) # 9, 상수

num1 = 4 # 정수 4를 num1이라는 변수에 저장
num2 = 5 # 정수 5를 num2이라는 변수에 저장
print(num1 + num2) # 9, 변수

num2 = 10
print(num1 + num2) # 14

# 문자 변수 선언
name = "이선화"
print(name) # 이선화

# 변수 이름 규칙
# 3num = 20 # 변수 이름은 숫자로 시작할 수 없음
# user id = "abc123" # 변수 이름에 공백이 포함될 수 없음
# for = 100 # for는 예약어이므로 변수 이름으로 사용할 수 없음

user_id = "abc123" 
print(user_id) # abc123

# 자료형 - 파이썬에서는 생략
print(type(num1)) # <class 'int'>
print(type(name)) # <class 'str'>
print(type(True)) # <class 'bool'>, 불리언 자료형

print(10 > 20) # False, 비교 연산자
print(type(10 > 20)) # <class 'bool'>

# print(10 == 20) # False, 비교 연산자
# print(type(10 == 20)) # <class 'bool'>

print(10 != 20) # True, 비교 연산자

