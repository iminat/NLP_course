import json

# Чтение данных из файла и обработка всего массива JSON
with open('result_december.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    # Убираем лишние символы, например, несколько пустых строк или пробелов
    content = content.strip()

    # Пытаемся распарсить весь файл как один массив JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Ошибка при парсинге файла: {e}")
        data = []


# Функция для очистки данных
def clean_data(data):
    # Список имен, которые нужно исключить
    excluded_senders = {"Егор Шиповников", "Яна Труш", "Иминат", "Юля ⛅️", "Alina Ivashkina",
                        "Анастасия Колотова"}

    cleaned = []
    for item in data:
        if "from" in item and "text" in item:
            sender = item["from"]
            text = item["text"]

            # Проверяем, если отправитель в списке исключений
            if sender in excluded_senders:
                continue  # Пропускаем эту запись

            # Проверяем, если text является списком, объединяем элементы в строку
            if isinstance(text, list):
                text = ''.join([part['text'] if isinstance(part, dict) else '' for part in text])
            # Если text является строкой, оставляем как есть
            elif isinstance(text, str):
                text = text
            # Добавляем запись, если текст не пустой
            if text.strip():
                cleaned.append({
                    "from": sender,
                    "text": text.strip()
                })
    return cleaned


# Очистка данных
cleaned_data = clean_data(data)

# Проверим очищенные данные и выведем их в консоль
if cleaned_data:
    print(f"Найдено {len(cleaned_data)} очищенных записей:")
    for item in cleaned_data:
        print(f"from: {item['from']} text: {item['text']}")
else:
    print("Нет данных для вывода.")
