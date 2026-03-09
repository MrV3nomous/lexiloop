
import time
from rich.console import Console
from rich.progress import Progress

console = Console()

class Color:
    GREEN = "green"
    RED = "red"
    YELLOW = "yellow"
    CYAN = "cyan"
    MAGENTA = "magenta"

def delay(seconds):
    time.sleep(seconds)

def print_colored(text, color, end="\n"):
    console.print(text, style=color, end=end)

def show_progress_bar(message, total=100, speed=0.01):
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{message}", total=total)
        for i in range(total):
            delay(speed)
            progress.update(task, advance=1)
