import time
import tkinter as tk

def custom_hash(data):
    hash_value = 0
    for char in data:  # Обрабатываем каждый символ строки
        hash_value += ord(char) ** 2  # Квадрат ASCII-кода символа
        hash_value %= 1000000  # Ограничиваем значение
    return str(hash_value)


# Пример использования
print(custom_hash("Hello, Blockchain!"))


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp  # Временная метка
        self.data = data  # Данные блока
        self.previous_hash = previous_hash  # Хэш предыдущего блока
        self.hash = self.calculate_hash()  # Хэш текущего блока

    def calculate_hash(self):
        return custom_hash(f"{self.timestamp}{self.data}{self.previous_hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(time.time(), "Генезис-блок", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]  # Последний блок в цепочке
        new_block = Block(time.time(), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            # Проверка: изменился ли текущий блок
            if current.hash != current.calculate_hash():
                return False
            # Проверка: совпадает ли хэш предыдущего блока
            if current.previous_hash != previous.hash:
                return False
        return True


class BlockExplorerGUI:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.root = tk.Tk()
        self.root.title("Блокчейн Эксплорер")
        self.create_ui()

    def create_ui(self):
        for i, block in enumerate(self.blockchain.chain):
            block_info = f"Блок {i}\nХэш: {block.hash}\nВремя: {block.timestamp}\nДанные: {block.data}"
            label = tk.Label(self.root, text=block_info, relief="solid", borderwidth=2, padx=10, pady=10)
            label.pack(pady=5)

    def run(self):
        self.root.mainloop()

# Демонстрация
blockchain = Blockchain()
blockchain.add_block("Данные 1")
blockchain.add_block("Данные 2")

app = BlockExplorerGUI(blockchain)
app.run()
