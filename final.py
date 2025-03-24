import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3
import random
import os

class PythonLearningTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Learning Tool")
        self.root.geometry("800x600")
        self.engine = pyttsx3.init()
        self.root.configure(bg="#cce5ff")

        self.users_file = "users.txt"
        self.current_user = None
        self.themes = {
            "Light": {"bg": "#ffffff", "fg": "#000000"},
            "Dark": {"bg": "#2e2e2e", "fg": "#ffffff"},
            "Warm": {"bg": "#ffefd5", "fg": "#5a3d2b"},
            "Cool": {"bg": "#d0f0f0", "fg": "#004d4d"}
        }
        self.current_theme = "Light"
        self.show_login_page()
        
    def apply_theme(self):
        theme = self.themes[self.current_theme]
        self.root.configure(bg=theme["bg"])

    def show_login_page(self):
        self.clear_frame()
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(pady=50)

        ttk.Label(self.login_frame, text="Login", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self.login_frame, text="Username:").pack()
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        ttk.Label(self.login_frame, text="Password:").pack()
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self.login_frame, text="Login", command=self.login).pack(pady=5)
        ttk.Button(self.login_frame, text="Sign Up", command=self.show_signup_page).pack(pady=5)
        self.create_theme_dropdown()

    def create_theme_dropdown(self):
        ttk.Label(self.root, text="Select Theme:").pack()
        self.theme_var = tk.StringVar(value=self.current_theme)
        theme_menu = ttk.Combobox(self.root, textvariable=self.theme_var, values=list(self.themes.keys()))
        theme_menu.pack(pady=5)
        theme_menu.bind("<<ComboboxSelected>>", self.change_theme)
    
    def change_theme(self, event):
        self.current_theme = self.theme_var.get()
        self.apply_theme()



    def show_signup_page(self):
        self.clear_frame()
        self.signup_frame = ttk.Frame(self.root)
        self.signup_frame.pack(pady=50)

        ttk.Label(self.signup_frame, text="Sign Up", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self.signup_frame, text="Username:").pack()
        self.signup_username_entry = ttk.Entry(self.signup_frame)
        self.signup_username_entry.pack(pady=5)

        ttk.Label(self.signup_frame, text="Password:").pack()
        self.signup_password_entry = ttk.Entry(self.signup_frame, show="*")
        self.signup_password_entry.pack(pady=5)

        ttk.Button(self.signup_frame, text="Create Account", command=self.signup).pack(pady=5)
        ttk.Button(self.signup_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if self.authenticate_user(username, password):
            self.current_user = username
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.learning_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        username = self.signup_username_entry.get().strip()
        password = self.signup_password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Sign Up Failed", "Username and password cannot be empty.")
            return
        
        if self.user_exists(username):
            messagebox.showerror("Sign Up Failed", "Username already exists.")
        else:
            with open(self.users_file, "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Sign Up Successful", "Account created! Please log in.")
            self.show_login_page()

    def authenticate_user(self, username, password):
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as file:
                for line in file:
                    stored_user, stored_pass = line.strip().split(",")
                    if stored_user == username and stored_pass == password:
                        return True
        return False

    def user_exists(self, username):
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as file:
                for line in file:
                    stored_user, _ = line.strip().split(",")
                    if stored_user == username:
                        return True
        return False

    

    
    def learning_screen(self):
        self.clear_frame()
        
        topics = [
            "Introduction", "Variables", "Data Types", "Loops", "Functions", "Conditional Statements", "Lists", "Tuples", "Dictionaries", "Classes and Objects"
        ]
        self.current_topic_index = 0
        
        self.topic_label = tk.Label(self.root, text=topics[self.current_topic_index], font=("Arial", 16))
        self.topic_label.pack(pady=10)
        
        self.content_text = tk.Text(self.root, height=10, wrap=tk.WORD)
        self.content_text.pack()
        
        self.speak_button = tk.Button(self.root, text="🔊 Hear", command=self.speak_content)
        self.speak_button.pack(pady=5)
        
        navigation_frame = tk.Frame(self.root)
        navigation_frame.pack(pady=10)
        
        tk.Button(navigation_frame, text="Previous", command=lambda: self.change_topic(-1)).grid(row=0, column=0, padx=5)
        tk.Button(navigation_frame, text="Next", command=lambda: self.change_topic(1)).grid(row=0, column=1, padx=5)
        
        tk.Button(self.root, text="Quiz", command=self.quiz_screen).pack(pady=5)
        tk.Button(self.root, text="Practice", command=self.practice_screen).pack(pady=5)
        
        self.load_content()
    
    def load_content(self):
        content_dict = {
            "Introduction": "Python is a popular programming language used for various applications.\nExample: print('Hello, World!')",
            "Variables": "Variables store data in Python.\nExample: x = 10\n       name = 'Alice'",
            "Data Types": "Python has different data types like int, float, and string.\nExample: num = 5 (int), pi = 3.14 (float), text = 'Hello' (string)",
            "Loops": "Loops help in repeating tasks.\nExample: for i in range(5):\n                print(i)",
            "Functions": "Functions help in code reusability.\nExample: def greet():\n                print('Hello!')\n                greet()",
            "Conditional Statements": "Python supports if, elif, and else conditions.\nExample: if x > 0:\n                print('Positive')\n            else:\n                print('Negative')",
            "Lists": "Lists store multiple values.\nExample: numbers = [1, 2, 3, 4, 5]\n       print(numbers[0])",
            "Tuples": "Tuples are immutable lists.\nExample: coords = (10, 20)\n       print(coords[0])",
            "Dictionaries": "Dictionaries store key-value pairs.\nExample: student = {'name': 'John', 'age': 20}\n       print(student['name'])",
            "Classes and Objects": "Python supports Object-Oriented Programming.\nExample: class Car:\n                def __init__(self, brand):\n                    self.brand = brand\n                def show_brand(self):\n                    print(self.brand)\n            my_car = Car('Toyota')\n            my_car.show_brand()"
        }
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, content_dict[self.topic_label.cget("text")])
    
    def speak_content(self):
        text = self.content_text.get(1.0, tk.END)
        self.engine.say(text)
        self.engine.runAndWait()

    def change_topic(self, direction):
        topics = [
            "Introduction", "Variables", "Data Types", "Loops", "Functions", "Conditional Statements", "Lists", "Tuples", "Dictionaries", "Classes and Objects"
        ]
        self.current_topic_index += direction
        
        if self.current_topic_index < 0:
            self.current_topic_index = 0
        elif self.current_topic_index >= len(topics):
            self.current_topic_index = len(topics) - 1
        
        self.topic_label.config(text=topics[self.current_topic_index])
        self.load_content()

  

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


#QUIZ SCREEN
    def quiz_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Quiz Section", font=("Arial", 16)).pack(pady=10)
        
        self.questions = [
            ("What is the output of print(2 * 3)?", ["5", "6", "8", "None"], "6"),
            ("Which data type is mutable?", ["Tuple", "String", "List", "Integer"], "List"),
            ("Which keyword is used to define a function?", ["define", "def", "func", "lambda"], "def"),
            ("What is the output of 2 ** 3?", ["5", "6", "8", "None"], "8"),
            ("Which data type is immutable?", ["List", "String", "Dictionary", "Set"], "String"),
            ("Which keyword is used to iterate over a sequence?", ["for", "while", "do", "next"], "for"),
            ("What is the output of 10 % 3?", ["1", "2", "3", "4"], "1"),
            ("Which data type is used to store key-value pairs?", ["List", "Tuple", "Dictionary", "Set"], "Dictionary"),
            ("Which keyword is used to exit a loop?", ["break", "continue", "exit", "stop"], "break"),
            ("What is the output of 'hello' + 'world'?", ["helloworld", "hello world", "hello+world", "hello world"], "helloworld")
        ]
        random.shuffle(self.questions)
        
        self.current_question_index = 0
        self.score = 0
        self.display_question()
    
    def display_question(self):
        self.clear_frame()
        if self.current_question_index < len(self.questions):
            question, options, answer = self.questions[self.current_question_index]
            
            tk.Label(self.root, text=question, font=("Arial", 12)).pack(pady=10)
            self.selected_answer = tk.StringVar(value=-1)
            
            for option in options:
                tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=option).pack()
            
            tk.Button(self.root, text="Submit", command=lambda: self.check_answer(answer)).pack(pady=5)
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.learning_screen()
    
    def check_answer(self, answer):
        if self.selected_answer.get() == answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! ✅")
        else:
            messagebox.showerror("Wrong!", f"The correct answer was {answer}. ❌")
        
        self.current_question_index += 1
        self.display_question()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
#PRACTICE SCREEN
    def practice_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Practice Problems", font=("Arial", 16)).pack(pady=10)
        
        self.problems = [
            ("Check if a number is prime", "def is_prime(n):\n    pass", "Use a loop to check divisibility."),
            ("Reverse a string", "def reverse_string(s):\n    pass", "Use slicing or a loop."),
            ("Find factorial of a number", "def factorial(n):\n    pass", "Use recursion or a loop."),
            ("Find the largest number in a list", "def find_max(lst):\n    pass", "Iterate through the list."),
            ("Check if a string is a palindrome", "def is_palindrome(s):\n    pass", "Compare the string with its reverse."),
            ("Find the GCD of two numbers", "def gcd(a, b):\n    pass", "Use the Euclidean algorithm."),
            ("Generate Fibonacci sequence", "def fibonacci(n):\n    pass", "Use recursion or iteration.")
        ]
        self.current_problem_index = 0
        self.solved_count = 0
        self.correct_count = 0
        self.display_problem()
        
        tk.Button(self.root, text="New Problem", command=self.new_problem).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.learning_screen).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="red", fg="white").pack(pady=5)  # Exit button

    def display_problem(self):
        self.clear_frame()
        problem, starter_code, hint = self.problems[self.current_problem_index]

        tk.Label(self.root, text=f"Problem {self.current_problem_index + 1}/{len(self.problems)}", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text=problem, font=("Arial", 14)).pack(pady=10)

        self.code_entry = tk.Text(self.root, height=5, width=50)
        self.code_entry.insert(tk.END, starter_code)
        self.code_entry.pack()

        tk.Button(self.root, text="Submit", command=self.evaluate_code).pack(pady=5)
        tk.Button(self.root, text="Hint", command=self.show_hint).pack(pady=5)

        navigation_frame = tk.Frame(self.root)
        navigation_frame.pack(pady=10)
        tk.Button(navigation_frame, text="Previous", command=lambda: self.change_problem(-1)).grid(row=0, column=0, padx=5)
        tk.Button(navigation_frame, text="Next", command=lambda: self.change_problem(1)).grid(row=0, column=1, padx=5)
        
        self.progress_label = tk.Label(self.root, text=f"Solved: {self.solved_count} | Correct: {self.correct_count}", font=("Arial", 12))
        self.progress_label.pack(pady=10)

    def change_problem(self, direction):
        self.current_problem_index += direction
        if self.current_problem_index < 0:
            self.current_problem_index = 0
        elif self.current_problem_index >= len(self.problems):
            self.current_problem_index = len(self.problems) - 1
        self.display_problem()

    def show_hint(self):
        _, _, hint = self.problems[self.current_problem_index]
        messagebox.showinfo("Hint", hint)

    def evaluate_code(self):
        user_code = self.code_entry.get("1.0", tk.END).strip()
        self.solved_count += 1  # Increment solved count for every attempt

        test_cases = {
            "Check if a number is prime": [(2, True), (4, False), (7, True)],
            "Reverse a string": [("hello", "olleh"), ("world", "dlrow")],
            "Find factorial of a number": [(3, 6), (5, 120)],
            "Find the largest number in a list": [([1, 2, 3, 4, 5], 5), ([10, 3, 8], 10)],
            "Check if a string is a palindrome": [("racecar", True), ("hello", False)],
            "Find the GCD of two numbers": [(10, 5, 5), (36, 24, 12)],
            "Generate Fibonacci sequence": [(5, [0, 1, 1, 2, 3])]
        }

        problem, _, _ = self.problems[self.current_problem_index]
        test_data = test_cases.get(problem, [])
        function_name = user_code.split("(")[0].split()[-1]  # Extract function name
        
        try:
            exec(user_code, globals())  # Execute user code
            for inputs, expected in test_data:
                result = eval(f"{function_name}({', '.join(map(str, inputs))})")
                if result != expected:
                    raise ValueError(f"Test case failed for input {inputs}. Expected {expected}, got {result}")
            self.correct_count += 1  # Increment only if all test cases pass
            messagebox.showinfo("Success", "All test cases passed! 🎉")
        except Exception as e:
            messagebox.showerror("Error", f"Your code failed: {e}")

        # Update progress label
        self.progress_label.config(text=f"Solved: {self.solved_count} | Correct: {self.correct_count}")


    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def speak_content(self):
        text = self.content_text.get(1.0, tk.END)
        self.engine.say(text)
        self.engine.runAndWait()

    

    
if __name__ == "__main__":
    root = tk.Tk()
    try:
        root.iconbitmap("icon.ico")
    except tk.TclError:
        print("Warning: icon.ico not found or not supported on this OS")
    app = PythonLearningTool(root)
    root.mainloop()
