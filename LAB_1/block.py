# block.py
import time
from hash_util import custom_hash


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
