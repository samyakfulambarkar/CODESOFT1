import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Instructions Label
        self.instructions_label = tk.Label(master, text="Choose rock, paper, or scissors:", font=("Arial", 14))
        self.instructions_label.pack(pady=10)

        # Buttons for user choices
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"), font=("Arial", 12))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"), font=("Arial", 12))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"),
                                         font=("Arial", 12))
        self.scissors_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Score Label
        self.score_label = tk.Label(master, text="Your Score: 0 | Computer Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, font=("Arial", 12))
        self.play_again_button.pack(pady=5)
        self.play_again_button.config(state=tk.DISABLED)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.display_choices(user_choice, computer_choice)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)
        self.update_scores(result)

    def display_choices(self, user_choice, computer_choice):
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_scores(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Your Score: 0 | Computer Score: 0")
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
