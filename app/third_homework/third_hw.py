from pathlib import Path
import sys
from colorama import Fore

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"{Fore.RED}Структура для: {path}")
        try:
            print_structure(path)
        except Exception as e:
            print(f"Помилка: {e}")
    else:
        print("Аргументи не передано.")

def print_structure(path, spaces=0):
    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]
    color = colors[spaces // 4 % len(colors)]
    for item in get_dir_items(path):
        print(f"{' ' * spaces}{color}|--{item.name}{Fore.RESET}")
        if item.is_dir():
            print_structure(item, spaces + 4)

def get_dir_items(path):
    items = []
    directory = Path(path)
    if not directory.exists():
        print("Шлях не існує.")
        return items
    items = directory.iterdir()
    return items


if __name__ == "__main__":
    main()