# 컴퓨터 용어 사전 만들기
print("컴퓨터 용어 사전")

dic = {
    "이진수": "0과 1로 이루어진 수 체계",
    "알고리즘": "문제를 해결하기 위한 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록"
}

while True:
    word = input("검색할 단어를 입력하세요 (종료: q or Q): ")
    if word == 'q' or word == 'Q':
        print("프로그램을 종료합니다.")
        break
    if word in dic: # 딕셔너리에 단어가 있는지 확인
        print(f"{word}: {dic[word]}")
    else:
        print("해당 단어를 찾을 수 없습니다.")