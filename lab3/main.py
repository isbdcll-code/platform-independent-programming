import json
from datetime import datetime
from pathlib import Path

# Путь к файлу с заметками
NOTES_FILE = Path('notes.json')


def load_notes():
    """Загрузка заметок из файла."""
    if not NOTES_FILE.exists():
        return []
    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_notes(notes):
    """Сохранение заметок в файл."""
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def create_note():
    """Создание новой заметки с автоматической датой."""
    print("\n--- Создание новой заметки ---")
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")

    # Автоматически добавляем текущую дату и время
    now = datetime.now()
    timestamp = now.strftime("%d.%m.%Y %H:%M:%S")

    new_note = {
        "title": title,
        "text": text,
        "date": timestamp
    }

    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно сохранена!")


def show_all_notes():
    """Вывод всех заметок."""
    notes = load_notes()
    if not notes:
        print("\nСписок заметок пуст.")
        return

    print(f"\n--- Список всех заметок (всего: {len(notes)}) ---")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. [{note['date']}] {note['title']}")
        print(f"   {note['text']}")
        print("-" * 20)


def find_notes_by_date():
    """Поиск заметки по дате."""
    date_input = input("\nВведите дату для поиска (ДД.ММ.ГГГГ): ")

    notes = load_notes()
    found_notes = []

    for note in notes:
        # Извлекаем только дату (первые 10 символов) для сравнения
        note_date = note['date'][:10]
        if note_date == date_input:
            found_notes.append(note)

    if not found_notes:
        print(f"Заметки на дату {date_input} не найдены.")
    else:
        print(f"\n--- Заметки за {date_input} ---")
        for note in found_notes:
            print(f"[{note['date']}] {note['title']}")
            print(f"Текст: {note['text']}")
            print("-" * 20)


def main():
    """Главное меню программы."""
    while True:
        print("\nМЕНЮ:")
        print("1 – Создать новую заметку")
        print("2 – Показать все заметки")
        print("3 – Найти заметку по дате")
        print("4 – Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            show_all_notes()
        elif choice == '3':
            find_notes_by_date()
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()