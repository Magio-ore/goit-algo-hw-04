from Data import data

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    path = "./Data/contact.txt"
    result = data.add_on_file(path, name, phone) 
    return result

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    path = "./Data/contact.txt"
    result = data.change_number_onfile(path, name, phone) 
    return result

def show_all():
    path = "./Data/contact.txt"
    result = data.read_file(path)
    return result

def show_phone(args):    
    name = args[0]
    path = "./Data/contact.txt"
    result = data.get_number(path, name)
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        # Команда виведення усіх даних з файлу
        elif command == "all":
            print (show_all())
        # Команда додавання користувача
        elif command == "add":
            if len(args) < 2:  # Перевіряємо, чи є два аргументи
                print("Please provide the contact name and phone number. Example: add John 1234567890")
            else:
                print(add_contact(args, contacts))
        # Команда зміни номеру користувача
        elif command == "change":
            if len(args) < 2:  # Перевіряємо, чи є два аргументи
                print("Please provide the contact name and phone number. Example: change John 1234567890")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) < 1:  # Перевіряємо, чи є два аргументи
                print("Please provide the contact name and phone number. Example: phone John")
            else:
                print(show_phone(args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
