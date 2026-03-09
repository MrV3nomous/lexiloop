import random
import threading
import time
from utils import Color, delay, print_colored

def get_human_input(last_char, used_words, valid_words):
    """Prompt human player for a word. Supports 'quit'."""
    while True:
        move = input(f"Enter a word starting with '{last_char}' (or type 'quit' to give up): ").lower().strip()
        if move == "quit":
            return "quit"
        if not move:
            print_colored("Enter something!", Color.RED)
            continue
        if move[0] != last_char:
            print_colored(f"Word must start with '{last_char}'!", Color.RED)
            continue
        if move in used_words:
            print_colored("Word already used!", Color.RED)
            continue
        if move not in valid_words:
            print_colored("Word not in dictionary!", Color.RED)
            continue
        return move


def ai_move(words_by_letter, used_words, last_char):
    """Smart AI move with continuous spinner and balanced difficulty."""
    possible = [w for w in words_by_letter.get(last_char, []) if w not in used_words]
    if not possible:
        return None

    # Spinner animation
    spinner_running = True
    spinner_chars = ['|', '/', '-', '\\']

    def spinner():
        i = 0
        while spinner_running:
            print_colored(f"AI is thinking {spinner_chars[i % len(spinner_chars)]}", Color.YELLOW, end='\r')
            i += 1
            time.sleep(0.15)

    spin_thread = threading.Thread(target=spinner)
    spin_thread.start()

    # --- AI logic ---
    # We assign a "score" to each possible move: higher score = safer for human, lower score = more challenging
    scored_moves = []
    for word in possible:
        next_last_char = word[-1]
        next_options = len([w for w in words_by_letter.get(next_last_char, []) if w not in used_words and w != word])

        # Add slight randomness to avoid AI always picking same pattern
        score = next_options + random.uniform(0, 1)
        scored_moves.append((score, word))

    # Sort moves by score: favor moves that don't create extreme traps, but still challenge player
    scored_moves.sort(key=lambda x: x[0], reverse=True)  # highest score = more options for player
    best_move = scored_moves[0][1] if scored_moves else random.choice(possible)

    # Stop spinner
    spinner_running = False
    spin_thread.join()
    print()  # newline after spinner

    print_colored(f"AI plays: {best_move}", Color.YELLOW)
    delay(0.3)
    return best_move
