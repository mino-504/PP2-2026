from tkinter import tk

window = tk.Tk()
window.title("Hello 최민호")
window.geometry("400x200")

label = tk.Label(window, text = "Hello tkinter")
label.pack()

window.mainloop()