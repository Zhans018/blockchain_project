# hash_util.py

def custom_hash(data):
    hash_value = 0
    for char in data:  # Обрабатываем каждый символ строки
        hash_value += ord(char) ** 2  # Квадрат ASCII-кода символа
        hash_value %= 1000000  # Ограничиваем значение
    return str(hash_value)
