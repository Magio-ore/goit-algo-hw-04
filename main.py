import os
import sys
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(root_dir, indent=''):
    try:
        # Перевірка чи шлях веде до директорії
        if not os.path.isdir(root_dir):
            raise NotADirectoryError(f"{root_dir} не є директорією")

        # Обхід вмісту директорії
        for item in os.listdir(root_dir):
            path = os.path.join(root_dir, item)
            if os.path.isdir(path):
                # Виведення імені директорії синім кольором
                print(Fore.BLUE + indent + item)
                print_directory_structure(path, indent + '    ')
            else:
                if item.endswith('.exe'):
                    # Виведення імені .exe файлів жовтим кольором
                    print(Fore.RED + indent + item)
                elif item.endswith('.py'):
                    # Виведення імені .py файлів зеленим кольором
                    print(Fore.CYAN + indent + item)
                else:
                    # Виведення імені інших файлів зеленим кольором
                    print(Fore.GREEN + indent + item)
    except FileNotFoundError:
        print(Fore.RED + f"Помилка: Шлях '{root_dir}' не знайдено.")
    except NotADirectoryError as e:
        print(Fore.RED + f"Помилка: {e}")
    except Exception as e:
        print(Fore.RED + f"Невідома помилка: {e}")

def main():
    # Перевірка аргументу командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)
    
    # Отримання шляху до директорії з аргументу командного рядка
    directory_path = sys.argv[1]
    
    # Виведення структури директорії
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
