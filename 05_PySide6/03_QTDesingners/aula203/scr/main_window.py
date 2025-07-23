import sys
from typing import cast

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

# Classe que representa a janela principal da aplicação
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)  # type: ignore

        self.lineName.installEventFilter(self)

    # Método que altera o texto do label com o texto do lineEdit
    def changeLabelResult(self):
        text = self.lineName.text()
        self.labelResult.setText(text)

    # Método que filtra eventos, neste caso, eventos de teclado
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            # Tenho certeza que o tipo é KeyPress
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()