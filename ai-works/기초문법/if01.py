# 조건문 - if문
# 조건 내용: 나이가 20세 미만이면 "미성년자입니다." 출력

# if문
"""
age = 19
if age < 20: # 조건이 참일때 실행
    print("미성년자입니다.")
"""

# if문 - else문
"""
age = 25
if age < 20:
    print("미성년자입니다.")
else: # 조건이 거짓일때 실행(else if >= 20)
    print("성인입니다.")
"""

# if문 - elif문(다중 조건)

# color = "초록", 입력 함수-input() 사용
color = input("신호등 색상을 입력하세요 (빨강, 노랑, 초록): ")

if color == "빨강":
    print("멈춤")
elif color == "노랑":
    print("주의")
elif color == "초록":
    print("진행")
else:
    print("알 수 없는 색입니다.")
