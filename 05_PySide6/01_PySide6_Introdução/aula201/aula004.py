# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv) # Cria a aplicação
window = QMainWindow() # Cria a janela principal
central_widget = QWidget() # Cria um widget central

window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Primeira Janela!')

botao1 = QPushButton('Título')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Título')
botao2.setStyleSheet('font-size: 80px;')

botao3 = QPushButton('Texto em linha')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1) # linha, coluna, linhas, colunas
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2) # Ocupa duas colunas

def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
menu.setStyleSheet("""
    QMenuBar::item {
        background: red;
        padding: 8px 24px;
        border-radius: 4px;
        color: #fff;
    }
    QMenuBar::item:selected {
        background: green;
        color: #f0f0f0;
    }
""")
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)

window.show()
app.exec()  # O loop da aplicação