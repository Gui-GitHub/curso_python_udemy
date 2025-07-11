# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
# pip install pyqtdarktheme

import qdarktheme
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


# def setupTheme():
#     """
#     Sets up the application's dark theme using qdarktheme with custom colors and additional QSS styles.
#     """
#     qdarktheme.setup_theme(
#         theme='dark',
#         corner_shape='rounded',
#         custom_colors={
#             "[dark]": {
#                 "primary": f"{PRIMARY_COLOR}",
#             },
#             "[light]": {
#                 "primary": f"{PRIMARY_COLOR}",
#             },
#         },
#         additional_qss=qss
#     )

def setupTheme():
    import qdarktheme
    from PySide6.QtWidgets import QApplication

    # Aplica o tema dark usando o método da versão 0.1.7
    QApplication.instance().setStyleSheet(
        qdarktheme.load_stylesheet()
        + qss  # Adiciona seu QSS customizado
    )