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
        self.charset = []

        # *Tkinter definitions
        self.title("Random Password Generator")
        self.geometry("800x190")
        self.resizable(False, False)
        self._set_window()

    def _set_window(self):
        """This private method determines the design of the GUI
        """
        # Define the main frame where all widgets will be placed
        root = tk.Frame(self)
        root.pack(fill=tk.BOTH, padx=5, pady=5)

        # Frame for the text field
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
            )
        password_text.pack(fill=tk.BOTH, padx=10, pady=10)

        # Framework for the definition of the password parameters.
        # Includes a scrollbar for the password length, a check box group for
        # the allowed character groups, and a button to generate the password.
        param_frame = tk.LabelFrame(root, text="Parameters")
        param_frame.pack(fill='both', padx=5, pady=5)

        scale_frame = tk.LabelFrame(param_frame, relief=tk.GROOVE)
        scale_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        pw_lenght = tk.Scale(
            scale_frame,
            from_=8, to=128,
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
            text="Uppercase Letters",
            variable=self.upper_c
            )
        lower_letters = tk.Checkbutton(
            check_box_frame,
            text="Lowercase Letters",
            variable=self.lower_c
            )
        numbers = tk.Checkbutton(
            check_box_frame,
            text="Numbers",
            variable=self.numbers
            )
        special_chars = tk.Checkbutton(
            check_box_frame,
            text="Punctuation",
            variable=self.special_c
            )
        upper_letters.grid(row=0, column=0, sticky='w')
        lower_letters.grid(row=0, column=1, sticky='w')
        numbers.grid(row=1, column=0, sticky='w')
        special_chars.grid(row=1, column=1, sticky='w')

        button_frame = tk.LabelFrame(param_frame, relief=tk.GROOVE)
        button_frame.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        def _add_to_textbox(entry: str):
            """This method unlocks the text field, deletes the text currently
            in it, inserts a new text and locks the text field again.

            Args:
                entry (str): Text to be inserted in the text field
            """
            password_text.configure(state=tk.NORMAL)
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, entry)
            password_text.configure(state=tk.DISABLED)

        def generate_pw():
            """This method first queries which character types are allowed,
            then generates the character set from which the password is
            generated
            """
            # Querying the check box states
            upper_c = self.upper_c.get()
            lower_c = self.lower_c.get()
            number_c = self.numbers.get()
            special_c = self.special_c.get()

            # Emptying the character set and creating a new one based on the
            # checkbox states
            self.charset = []
            if upper_c is True:
                self.charset += [u for u in string.ascii_uppercase]
            if lower_c is True:
                self.charset += [lower for lower in string.ascii_lowercase]
            if number_c is True:
                self.charset += [str(n) for n in range(0, 10)]
            if special_c is True:
                self.charset += [c for c in string.punctuation]

            # For loop that jpoins the selected number of random characters
            # from the character set to a string, including catching an
            # IndexError if the character set is empty. Finally, output the
            # password in the text field
            pw = ""
            try:
                for _ in range(self.len_pw.get()):
                    pw += random.choice(self.charset)
            except IndexError:
                _add_to_textbox(
                    "Please select at least one allowed character group first"
                    )
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
