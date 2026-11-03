import tkinter as tk

root = tk.Tk()
root.title("Oobutton")
root.geometry("600x400")

def on_label_clicked(event):  #이벤트 종류
    print(f"라벨이 클릭되었습니다: {event}")

label = tk.Label(root, text="객체지향윈도우프로그래밍")
label.bind("<Double-1>", on_label_clicked) #바인드 중요
label.pack()

def on_btn1_clicked(event):
    print(f"버튼1이 클릭되었습니다 : {event}")
    label.config(text = f"버튼1이 클릭되었습니다. {event}")

#btn1 = tk.Button(root, text="클릭해볼까요?", command = on_btn1_clicked)
btn1 = tk.Button(root, text="클릭해볼까요?", width = "100", height=50, fg = "red", bg="black")
btn1.bind("<Button-1>", on_btn1_clicked)
btn1.pack()


root.mainloop()