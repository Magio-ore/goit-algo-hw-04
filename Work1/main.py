from pathlib import PurePath, Path

path = PurePath("./salary_file.txt")

def total_salary(path):
    if Path(path).exists():  # Перевірка, чи існує файл
        total = 0
        line_count = 0
        with open(path, 'r') as file:
            for line in file:
                # Розділяємо рядок по комі
                parts = line.strip().split(',')
                if len(parts) > 1:
                    try:
                        value = int(parts[1].strip())
                        total += value
                        line_count += 1 # Додаємо кількість рядків, щоб отримати середнє значення
                    except ValueError:
                        print(f"Помилка перетворення у числовий формат: '{parts[1].strip()}'")
                else:
                    # Якщо коми немає, виводимо повідомлення
                    print("У рядку немає коми або частини після неї")

        # Обчислення середнього значення
        if line_count > 0:
            average = total // line_count 
        else:
            average = 0  # Якщо немає жодного рядка з даними після коми

        return total, average
    else:
        print("Файл не знайдено!")
        return None, None

# Виклик функції
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
