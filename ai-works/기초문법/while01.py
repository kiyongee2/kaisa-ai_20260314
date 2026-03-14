"""
a = 1
print(a)

a = a + 1
print(a)

a += 1 # a = a + 1과 동일
print(a)
"""

'''
n = 1 #초기값
while n <= 5:
    print(n)
    n = n + 1
print("반복문 종료")
'''

# While문 - break문
n = 1
while True: # 무한 루프
    if n > 5:
        break # 반복문 종료
    print(n)
    n = n + 1

print("반복문 종료") # 이 부분은 실행되지 않음