from pathlib import PurePath, Path

path = PurePath("./cats_file.txt")

def get_cats_info(path):
    if Path(path).exists():  # Перевірка, чи існує файл
        cats_info = [] 
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                # Розділяємо рядок по комі
                parts = line.strip().split(',')
                
                # Перевіряємо, що рядок має три частини
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0].strip(),
                        "name": parts[1].strip(),
                        "age": parts[2].strip()
                    }
                    cats_info.append(cat_dict)
                else:
                    print(f"Рядок {parts} містить більше ніж 3 частини")
        
        return cats_info
    else:
        print("Файл не знайдено або він пошкоджений!")
        return None

# Виклик функції
cats_info = get_cats_info(path)
print(cats_info)
