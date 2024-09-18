from pathlib import Path, PurePath

path = PurePath("./Data/contact.txt")

# Читаємо усі дані в файлі і виводимо їх
def read_file(path):
    if Path(path).exists():  # Перевірка, чи існує файл
        with open(path, 'r') as file:
            file_read = file.read()
            return file_read
    return "File does not exist."

# Додаємо контакт в довідник
def add_on_file(path, name, phone):
    # Зчитуємо всі контакти з файлу
    contacts = {}
    if Path(path).exists():
        with open(path, 'r') as file:
            for line in file:
                if line.strip():
                    contact_name, contact_phone = line.strip().split(': ')
                    contacts[contact_name] = contact_phone

    # Перевіряємо, чи існує контакт з таким ім'ям
    if name in contacts:
        return "Contact already exists."
    
    # Оновлюємо або додаємо контакт
    contacts[name] = phone

    # Перезаписуємо файл
    with open(path, 'w') as file:
        for contact_name, contact_phone in contacts.items():
            file.write(f"{contact_name}: {contact_phone}\n")

    return "Contact added"

# Зміна номеру телефону
def change_number_onfile(path, name, phone):
    contacts = {}
    
    # Зчитуємо всі контакти з файлу
    if Path(path).exists():
        with open(path, 'r') as file:
            for line in file:
                if line.strip():
                    contact_name, contact_phone = line.strip().split(': ')
                    contacts[contact_name] = contact_phone

    # Оновлюємо контакт
    contacts[name] = phone

    # Перезаписуємо файл
    with open(path, 'w') as file:
        for contact_name, contact_phone in contacts.items():
            file.write(f"{contact_name}: {contact_phone}\n")

    return "Contact updated."

# Виведення номеру телефону по імені
def get_number(path, name):
    contacts = {}
    
    if Path(path).exists():
        with open(path, 'r') as file:
            for line in file:
                if line.strip():
                    try:
                        contact_name, contact_phone = line.strip().split(': ')
                        contacts[contact_name] = contact_phone
                    except ValueError:
                        print(f"Skipping invalid line: {line.strip()}")
    else:
        return "File does not exist."
    
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"The user with the name {name} does not exist in the system"