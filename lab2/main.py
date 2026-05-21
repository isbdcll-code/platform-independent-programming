import pathlib
import datetime
from typing import List, Dict, Tuple

DATA_DIR = pathlib.Path('data')
JOURNAL_FILE = DATA_DIR / 'journal.txt'

DATA_DIR.mkdir(exist_ok=True)

def get_valid_date() -> str:
    while True:
        date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Ошибка: Неверный формат даты. Используйте ГГГГ-ММ-ДД.")

def get_valid_rating() -> int:
    while True:
        try:
            rating = int(input("Введите оценку (1-10): "))
            if 1 <= rating <= 10:
                return rating
            else:
                print("Ошибка: Оценка должна быть от 1 до 10.")
        except ValueError:
            print("Ошибка: Введите целое число.")

# --- Journal Operations ---
def add_entry():
    print("\n--- Добавление новой записи ---")
    date = get_valid_date()
    text = input("Введите текст наблюдения: ")
    rating = get_valid_rating()

    try:
        with JOURNAL_FILE.open('a', encoding='utf-8') as f:
            f.write(f"{date} | {rating} | {text}\n")
        print("Запись успешно добавлена!")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")

def read_entries() -> List[Dict[str, str]]:
    entries = []
    if not JOURNAL_FILE.exists():
        return entries

    try:
        with JOURNAL_FILE.open('r', encoding='utf-8') as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split('|')]
                if len(parts) == 3:
                    entries.append({
                        'date': parts[0],
                        'rating': int(parts[1]),
                        'text': parts[2]
                    })
        return entries
    except FileNotFoundError:
        print("Файл журнала не найден.")
        return []
    except ValueError:
        print("Ошибка: Некорректный формат данных в файле журнала.")
        return []
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def show_entries():
    print("\n--- Все записи ---")
    entries = read_entries()

    if not entries:
        print("Журнал пока пуст.")
        return

    date_width = max(len('Дата'), max(len(e['date']) for e in entries))
    rating_width = max(len('Оценка'), max(len(str(e['rating'])) for e in entries))
    text_width = max(len('Текст'), max(len(e['text']) for e in entries))

    # Table header
    header_line = '+' + '-' * (date_width + 2) + '+' + '-' * (rating_width + 2) + '+' + '-' * (text_width + 2) + '+'
    header_text = f"| {'Дата':<{date_width}} | {'Оценка':^{rating_width}} | {'Текст':<{text_width}} |"
    print(header_line)
    print(header_text)
    print(header_line)

    total_rating = 0
    for entry in entries:
        print(f"| {entry['date']:<{date_width}} | {entry['rating']:^{rating_width}} | {entry['text']:<{text_width}} |")
        total_rating += entry['rating']
    print(header_line)

    num_entries = len(entries)
    average_rating = total_rating / num_entries if num_entries > 0 else 0

    print("\nСтатистика:")
    print(f"Всего записей: {num_entries}")
    print(f"Средняя оценка: {average_rating:.2f}")

def clear_journal():
    try:
        if JOURNAL_FILE.exists():
            JOURNAL_FILE.write_text('', encoding='utf-8')  # Truncate file
            print("Журнал успешно очищен.")
        else:
            print("Журнал не существует или уже пуст.")
    except IOError as e:
        print(f"Ошибка при очистке журнала: {e}")

def display_menu():
    print("\n" + "=" * 40)
    print("        ЖУРНАЛ НАБЛЮДЕНИЙ")
    print("=" * 40)
    print("Выберите действие:")
    print("1. Добавить запись")
    print("2. Показать все записи")
    print("3. Очистить журнал")
    print("4. Выход")

def main():
    while True:
        display_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            show_entries()
        elif choice == '3':
            clear_journal()
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

if __name__ == '__main__':
    main()
