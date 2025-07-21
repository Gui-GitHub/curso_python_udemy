# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Título')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Título')
botao2.setStyleSheet('font-size: 80px;')

botao3 = QPushButton('Texto em linha')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget() # Cria um widget central
layout = QGridLayout()
central_widget.setLayout(layout)

# Adiciona os botões ao layout
layout.addWidget(botao, 1, 1, 1, 1) # linha, coluna, linhas, colunas
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2) # Ocupa duas colunas

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação