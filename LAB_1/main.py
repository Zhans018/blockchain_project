# main.py
from block import Blockchain
from block_explorer_gui import BlockExplorerGUI

# Демонстрация
blockchain = Blockchain()
blockchain.add_block("Данные 1")
blockchain.add_block("Данные 2")

app = BlockExplorerGUI(blockchain)
app.run()
