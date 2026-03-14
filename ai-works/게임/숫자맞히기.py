import random

# 1. 컴퓨터가 1 ~ 100 사이의 랜덤 숫자를 생성한다.
answer = random.randint(1, 100)
tries = 0

print("숫자 맞추기 게임에 오신 것을 환영합니다!")
print("1부터 100 사이의 숫자를 맞혀 보세요.")

# 2. 사용자가 숫자를 입력한다.
while True:
    tries += 1
    try:
        guess = int(input(f"{tries}번째 시도: "))
    except ValueError:
        print("유효한 숫자를 입력해 주세요.")
        continue

    # 3. 입력한 숫자가 큰지/작은지 비교한다.
    if guess < answer:
        print("입력한 수가 더 작아요")
    elif guess > answer:
        print("입력한 수가 더 커요")
    else:
        # 4. 숫자를 맞히면 시도 횟수를 출력하고 종료한다.
        print(f"정답입니다! {tries}번 만에 맞추셨습니다.")
        break
