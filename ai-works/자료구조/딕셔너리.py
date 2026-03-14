# 딕셔너리 - 키(속성)와 value(값)의 쌍으로 이루어진 자료형
# 딕셔너리는 중괄호 {}로 감싸서 표현하며, 키와 값은 콜론 :으로 구분한다.
student = {
    'name': '홍길동', 
    'age': 20,
}

print(student)  # {'name': '홍길동', 'age': 20}
print(type(student))  # <class 'dict'>

# 딕셔너리의 요소에 접근(검색) - 키 사용
print(student['name'])  # 홍길동
print(student['age'])   # 20

# 딕셔너리의 요소 추가 
student['major'] = '컴퓨터공학'
print(student)  # {'name': '홍길동', 'age': 20, 'major': '컴퓨터공학'}

# 딕셔너리의 요소 변경
student['age'] = 24
print(student)  # {'name': '홍길동', 'age': 24, 'major': '컴퓨터공학'}