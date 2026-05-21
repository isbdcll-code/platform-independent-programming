import datetime

def create_business_card():
    print("*" * 40)
    print("*" + "Личная визитка".center(38) + "*")
    print("*" * 40)

    # Ввод данных
    try:
        first_name = input("Введите ваше имя: ")
        last_name = input("Введите вашу фамилию: ")
        birth_year = int(input("Введите год рождения: "))
        height = float(input("Введите ваш рост (см): "))

        # Вычисление возраста
        current_year = datetime.date.today().year
        age = current_year - birth_year

        # Подготовка строк для визитки
        lines = [
            f"Имя: {first_name}",
            f"Фамилия: {last_name}",
            f"Год рождения: {birth_year}",
            f"Возраст: {age} лет",
            f"Рост: {height} см"
        ]

        # Вывод визитки
        print("\n" + "*" * 40)
        print("*" + "ВАША ВИЗИТКА".center(38) + "*")
        print("*" * 40)

        for line in lines:
            print(f"* {line:<36} *")

        print("*" * 40)

    except ValueError:
        print("Ошибка: Пожалуйста, вводите числовые значения для года рождения и роста.")

if __name__ == "__main__":
    create_business_card()