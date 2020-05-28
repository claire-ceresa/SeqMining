from PyQt5 import QtWidgets, QtGui


def fill_combobox(combobox, list):
    """Fill in a QComboBox"""
    combobox.clear()
    for name in list:
        combobox.addItem(str(name))


def create_messageBox(title, text):
    """Create and execute a QMessageBox"""
    message = QtWidgets.QMessageBox()
    message.setText(text)
    message.setWindowTitle(title)
    message.exec()


def create_label(text):
    label = QtWidgets.QLabel()
    label.setText(text)
    return label


def set_label_bold(label, bool):
    font = QtGui.QFont()
    font.setBold(bool)
    label.setFont(font)


def create_layout(widgets=None, vertical=False, horizontal=False):
    if vertical and not horizontal:
        layout = QtWidgets.QVBoxLayout()
    elif horizontal and not vertical:
        layout = QtWidgets.QHBoxLayout()
    else:
        layout = QtWidgets.QBoxLayout()

    if widgets is not None:
        for widget in widgets:
            if isinstance(widget, QtWidgets.QBoxLayout):
                layout.addLayout(widget)
            else:
                layout.addWidget(widget)
        spacer = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacer)

    return layout

