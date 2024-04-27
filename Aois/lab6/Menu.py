import  hash_table
def menu():
    hash_tabl = hash_table.HashTable()
    while True:
        print("\n1. Вставить элемент")
        print("2. Найти элемент")
        print("3. Удалить элемент")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            hash_tabl.insert(key, value)
        elif choice == '2':
            key = input("Введите ключ: ")
            value = hash_tabl.find(key)
            if value is None:
                print("Элемент не найден")
            else:
                print(f"Значение: {value}")
        elif choice == '3':
            key = input("Введите ключ: ")
            value = hash_tabl.remove(key)
            if value is None:
                print("Элемент не найден")
            else:
                print(f"Удален элемент со значением: {value}")
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    menu()