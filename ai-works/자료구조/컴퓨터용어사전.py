import tkinter as tk
from tkinter import messagebox

# 컴퓨터 용어 사전
dic = {
    "이진수": "0과 1로 이루어진 수 체계",
    "알고리즘": "문제를 해결하기 위한 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
}


def 검색():
    word = entry.get().strip()
    if not word:
        messagebox.showinfo("알림", "검색할 단어를 입력하세요.")
        return

    if word in dic:
        result_var.set(f"{word}: {dic[word]}")
    else:
        result_var.set("해당 단어를 찾을 수 없습니다.")


def 종료():
    root.destroy()


root = tk.Tk()
root.title("컴퓨터 용어 사전")

# 입력 영역
tk.Label(root, text="검색할 단어:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=8, pady=8)
entry.focus()

# 버튼
tk.Button(root, text="검색", command=검색).grid(row=0, column=2, padx=8, pady=8)
tk.Button(root, text="종료", command=종료).grid(row=1, column=2, padx=8, pady=8)

# 결과 표시
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").grid(row=1, column=0, columnspan=2, padx=8, pady=8, sticky="w")

root.mainloop()
