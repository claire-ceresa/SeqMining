from PyQt5.QtWidgets import QMessageBox


def fill_combobox(combobox, list):
    """Fill in a QComboBox"""
    for name in list:
        combobox.addItem(str(name))


def create_messageBox(title, text):
    """Create and execute a QMessageBox"""
    message = QMessageBox()
    message.setText(text)
    message.setWindowTitle(title)
    message.exec()


