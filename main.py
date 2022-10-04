# main.py

'''
A random password generator using python and tkinter library
'''


import string
import random
import tkinter as tk


class RandomPasswordGenerator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.len_pw = tk.IntVar()
        self.upper_c = tk.BooleanVar()
        self.lower_c = tk.BooleanVar()
        self.numbers = tk.BooleanVar()
        self.special_c = tk.BooleanVar()
        self.title("Random Password Generator")
        self.geometry("800x220")
        self.resizable(False, False)
        self._set_window()

    def _set_window(self):
        root = tk.Frame(self)
        root.pack(fill=tk.BOTH, padx=5, pady=5)

        text_frame = tk.LabelFrame(
            root,
            relief=tk.GROOVE,
            text="Your Password"
            )
        text_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        password_text = tk.Text(
            text_frame,
            height=1,
            state=tk.DISABLED,
            font=('Times New Roman', 24, 'bold')
            )
        password_text.pack(fill=tk.BOTH, padx=10, pady=10)

        param_frame = tk.LabelFrame(root, text="Parameters")
        param_frame.pack(fill='both', padx=5, pady=5)

        scale_frame = tk.LabelFrame(param_frame, relief=tk.GROOVE)
        scale_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        pw_lenght = tk.Scale(
            scale_frame,
            from_=16, to=256,
            orient='horizontal',
            length=360,
            label="Choose password lenght",
            variable=self.len_pw,
            )
        pw_lenght.pack(fill='x', padx=5, pady=5)

        check_box_frame = tk.LabelFrame(param_frame, relief=tk.GROOVE)
        check_box_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        upper_letters = tk.Checkbutton(
            check_box_frame,
            text="Uppercase letters",
            variable=self.upper_c
            )
        lower_letters = tk.Checkbutton(
            check_box_frame,
            text="Lowercase letters",
            variable=self.lower_c
            )
        numbers = tk.Checkbutton(
            check_box_frame,
            text="Numbers",
            variable=self.numbers
            )
        special_chars = tk.Checkbutton(
            check_box_frame,
            text="Special Characters",
            variable=self.special_c
            )
        upper_letters.grid(row=0, column=0, sticky='w')
        lower_letters.grid(row=0, column=1, sticky='w')
        numbers.grid(row=1, column=0, sticky='w')
        special_chars.grid(row=1, column=1, sticky='w')

        button_frame = tk.LabelFrame(param_frame, relief=tk.GROOVE)
        button_frame.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        def _add_to_textbox(entry):
            password_text.configure(state=tk.NORMAL)
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, entry)
            password_text.configure(state=tk.DISABLED)

        def generate_pw():
            upper_c = self.upper_c.get()
            lower_c = self.lower_c.get()
            number_c = self.numbers.get()
            special_c = self.special_c.get()
            charset = []
            if upper_c is True:
                u_letters = [u for u in string.ascii_uppercase]
                charset += u_letters
            if lower_c is True:
                l_letters = [lower for lower in string.ascii_lowercase]
                charset += l_letters
            if number_c is True:
                nums = [str(n) for n in range(0, 10)]
                charset += nums
            if special_c is True:
                s_chars = [c for c in string.punctuation]
                charset += s_chars
            pw = ""
            try:
                for _ in range(self.len_pw.get()):
                    pw += random.choice(charset)
            except IndexError:
                _add_to_textbox("Please select elemnets for charset")
                return
            _add_to_textbox(pw)

        gen_button = tk.Button(
            button_frame,
            text="Generate",
            font=('Arial', 16),
            command=generate_pw
            )
        gen_button.pack(padx=5, pady=5, fill='both', expand=True)


def main():
    random_password = RandomPasswordGenerator()
    random_password.mainloop()


if __name__ == '__main__':
    main()
