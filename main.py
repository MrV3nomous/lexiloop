from utils import show_progress_bar, Color, print_colored
from game import LexiLoopGame

def load_words(file_path="datasets/words.txt"):
    with open(file_path, "r") as f:
        words = [line.strip().lower() for line in f if line.strip()]
    return words

def main():
    print_colored("Welcome to LexiLoop!", Color.CYAN)
    print("Choose mode: 1) Single Player  2) Two Player")
    choice = input("> ").strip()
    two_player = choice == "2"

    print_colored("Loading word dataset...", Color.YELLOW)
    show_progress_bar("Preloading words", total=50, speed=0.01)
    words = load_words()

    game = LexiLoopGame(words)
    game.play(two_player=two_player)

    print_colored("Thanks for playing LexiLoop!", Color.GREEN)

if __name__ == "__main__":
    main()
