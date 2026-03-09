from utils import Color, print_colored
from player import get_human_input, ai_move
import random

class LexiLoopGame:
    def __init__(self, words):
        self.words = words
        self.used_words = set()
        self.words_by_letter = self._organize_words_by_letter()
        self.valid_words = set(words)

    def _organize_words_by_letter(self):
        """Organize words by their starting letter for fast lookup."""
        d = {}
        for word in self.words:
            if word:
                d.setdefault(word[0], []).append(word)
        return d

    def play(self, two_player=False):
        print_colored("Starting LexiLoop!", Color.GREEN)
        start_word = random.choice(self.words)
        self.used_words.add(start_word)
        last_char = start_word[-1]
        print_colored(f"Starting word: {start_word}", Color.GREEN)

        turn = "human1"

        while True:
            if turn == "human1":
                move = get_human_input(last_char, self.used_words, self.valid_words)
                if move == "quit":
                    print_colored("Player gave up! Game over.", Color.RED)
                    break
                print_colored(f"Player 1 chose: {move}", Color.CYAN)
                self.used_words.add(move)
                last_char = move[-1]
                turn = "ai" if not two_player else "human2"

            elif turn == "human2":
                move = get_human_input(last_char, self.used_words, self.valid_words)
                if move == "quit":
                    print_colored("Player 2 gave up! Game over.", Color.RED)
                    break
                print_colored(f"Player 2 chose: {move}", Color.MAGENTA)
                self.used_words.add(move)
                last_char = move[-1]
                turn = "human1"

            elif turn == "ai":
                move = ai_move(self.words_by_letter, self.used_words, last_char)
                if move is None:
                    print_colored("AI cannot find a valid word. You win!", Color.GREEN)
                    break
                self.used_words.add(move)
                last_char = move[-1]
                turn = "human1"
