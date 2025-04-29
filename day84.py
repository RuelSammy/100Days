#Calculator app
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=30, bd=10, insertwidth=2, bg="powder blue", justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, bg="grey")
        btns_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                tk.Button(
                    btns_frame, text=char, fg="black", font=('arial', 18, 'bold'),
                    height=2, width=7, bd=1, bg="#fff",
                    command=lambda ch=char: self.on_button_click(ch)
                ).grid(row=r, column=c)

        clear_btn = tk.Button(
            self.root, text="Clear", fg="white", bg="red", font=('arial', 18, 'bold'),
            command=self.clear
        )
        clear_btn.pack(fill='both')

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == '__main__':
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
