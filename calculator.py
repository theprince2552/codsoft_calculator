import tkinter as tk

class EnhancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_input = ""
        self.result_var = tk.StringVar()

        # Display
        self.display = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Create buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""
            self.result_var.set("")
        elif char == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.result_var.set(self.current_input)
            except Exception:
                self.result_var.set("Error")
                self.current_input = ""
        else:
            self.current_input += char
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = EnhancedCalculator(root)
    root.mainloop()
