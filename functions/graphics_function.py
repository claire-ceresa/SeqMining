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


def create_label(text=None, wordwrap=True):
    """Create and return a QLabel with the text setted"""
    label = QtWidgets.QLabel()
    label.setText(text)
    if wordwrap:
        label.setWordWrap(True)
    else:
        label.setWordWrap(False)
    return label


def set_label_bold(label, bool):
    """Set a QLabel in bold or not"""
    font = QtGui.QFont()
    font.setBold(bool)
    label.setFont(font)


def create_layout(widgets=None, vertical=False, horizontal=False, spacer=False):
    """Create, fill in and return a QLayout"""
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

        if spacer:
            spacer = QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            layout.addItem(spacer)

    return layout


def create_scroll_area(widget):
    area = QtWidgets.QScrollArea()
    area.setWidgetResizable(True)
    area.setWidget(widget)
    return area


def create_groupbox(title, flat=False):
    groupbox = QtWidgets.QGroupBox()
    groupbox.setTitle(title)
    layout = create_layout(vertical=True, spacer=False)
    groupbox.setLayout(layout)
    if flat:
        groupbox.setFlat(True)
    return groupbox

def add_widget_to_groupbox(widget, groupbox):
    layout = groupbox.layout()
    layout.addWidget(widget)


