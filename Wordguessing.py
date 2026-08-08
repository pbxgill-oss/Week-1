import random
import string


class WordGuessingGame:

    def __init__(self, max_lives=6):
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]

        self.secret = random.choice(self.words)
        self.blanks = ["_" for _ in self.secret]
        self.lives = max_lives
        self.used_letters = set()

    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("→ Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print("→ You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        found_any = False

        for i, ch in enumerate(self.secret):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self):
        return "_" not in self.blanks

    def display_word(self):
        print(" ".join(self.blanks))

    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret)} letters.")
        self.display_word()

        while True:
            # Ask the player for a letter
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check whether the letter is in the word
            if self.reveal_letters(guess):
                print("\nWell done, nice job! You found a letter.")
                self.display_word()

                # Check if the whole word has been guessed
                if self.all_blanks_filled():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret}")
                    print("GAME OVER")
                    break

            else:
                self.lives -= 1

                print(f"\n Nope. You lose a life. Lives left: {self.lives}")
                self.display_word()

                # Check if the player has run out of lives
                if self.lives <= 0:
                    print("\n Out of lives! Sad story!")
                    print(f"The word was: {self.secret}")
                    print("GAME OVER")
                    break


# Create an object
game = WordGuessingGame()

# Start the game
game.play()