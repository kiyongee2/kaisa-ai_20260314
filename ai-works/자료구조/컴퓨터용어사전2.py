import tkinter as tk
from tkinter import messagebox

# 컴퓨터 용어 사전 (확장)
dic = {
    "이진수": "0과 1로 이루어진 수 체계",
    "알고리즘": "문제를 해결하기 위한 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
    "변수": "값을 저장하기 위해 이름을 붙인 메모리 공간",
    "리스트": "여러 값을 순서대로 저장하는 자료구조",
    "딕셔너리": "키와 값의 쌍으로 데이터를 저장하는 자료구조",
    "클래스": "데이터와 기능을 하나로 묶은 사용자 정의 타입",
    "모듈": "파이썬 코드가 들어있는 파일로 재사용 가능",
    "패키지": "모듈을 모아둔 디렉터리",
    "인터프리터": "코드를 한 줄씩 읽고 실행하는 실행기",
    "컴파일": "코드를 기계가 실행할 수 있는 형태로 번역하는 과정",
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


def 추가():
    word = entry.get().strip()
    definition = entry_def.get("1.0", "end").strip()

    if not word or not definition:
        messagebox.showinfo("알림", "추가할 단어와 정의를 모두 입력하세요.")
        return

    if word in dic:
        messagebox.showinfo("알림", f"'{word}'은(는) 이미 사전에 존재합니다.")
        return

    dic[word] = definition
    result_var.set(f"추가됨: {word}: {definition}")

    entry.delete(0, "end")
    entry_def.delete("1.0", "end")
    entry.focus()


def 종료():
    root.destroy()


root = tk.Tk()
root.title("컴퓨터 용어 사전 2")
root.geometry("400x280")
root.resizable(False, False)

# 디자인 (글꼴, 색상)
font_label = ("맑은 고딕", 11)
font_entry = ("맑은 고딕", 11)
font_button = ("맑은 고딕", 10, "bold")
font_result = ("맑은 고딕", 11)

# 입력 영역
frame_top = tk.Frame(root, padx=12, pady=12, bg="#f5f5f5")
frame_top.pack(fill="x")
frame_top.columnconfigure(1, weight=1)

label = tk.Label(frame_top, text="검색할 단어:", font=font_label, bg="#f5f5f5")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame_top, width=24, font=font_entry)
entry.grid(row=0, column=1, padx=8, sticky="ew")
entry.focus()

label_def = tk.Label(frame_top, text="정의:", font=font_label, bg="#f5f5f5")
label_def.grid(row=1, column=0, sticky="nw", pady=(8, 0))

entry_def = tk.Text(frame_top, width=28, height=3, font=font_entry, wrap="word")
entry_def.grid(row=1, column=1, padx=8, pady=(8, 0), sticky="ew")

button_search = tk.Button(frame_top, text="검색", width=10, font=font_button, bg="#4a90e2", fg="white", command=검색)
button_search.grid(row=0, column=2, padx=4)

button_quit = tk.Button(frame_top, text="종료", width=10, font=font_button, bg="#d9534f", fg="white", command=종료)
button_quit.grid(row=0, column=3, padx=4)

button_add = tk.Button(frame_top, text="추가", width=10, font=font_button, bg="#5cb85c", fg="white", command=추가)
button_add.grid(row=1, column=3, padx=4, pady=(8, 0))

# 결과 영역
frame_bottom = tk.Frame(root, padx=12, pady=12, bg="#ffffff")
frame_bottom.pack(fill="both", expand=True)

result_var = tk.StringVar()
result_label = tk.Label(frame_bottom, textvariable=result_var, font=font_result, fg="#333333", bg="#ffffff", justify="left", wraplength=360)
result_label.pack(anchor="w")

root.mainloop()
