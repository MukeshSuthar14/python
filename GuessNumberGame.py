import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                messagebox.showinfo("Success", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            print(ValueError)
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
