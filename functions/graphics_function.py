import os
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


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


def create_scroll_area(widget, minwidth=None, frame=True):
    area = QtWidgets.QScrollArea()
    area.setWidgetResizable(True)
    if minwidth is not None:
        area.setMinimumWidth(minwidth)
    if not frame:
        area.setFrameShape(QtWidgets.QFrame.NoFrame)
    area.setWidget(widget)
    return area


def create_groupbox(title=None, flat=False):
    groupbox = QtWidgets.QGroupBox()
    if title is not None:
        groupbox.setTitle(title)
    layout = create_layout(vertical=True, spacer=False)
    groupbox.setLayout(layout)
    if flat:
        groupbox.setFlat(True)
    return groupbox


def add_widget_to_groupbox(widget, groupbox):
    layout = groupbox.layout()
    layout.addWidget(widget)


def get_save_filename(type):
    if type == "Excel":
        filter = "Excel (*.xlsx)"
    elif type == "Text":
        filter = "Text (*.txt)"
    else:
        filter = None

    try:
        desktop_path = os.environ['USERPROFILE'] + '\Desktop\\'
        name = QtWidgets.QFileDialog.getSaveFileName(caption="Enregistrer", directory=desktop_path, filter=filter)
    except:
        name = QtWidgets.QFileDialog.getSaveFileName(caption='Enregister', filter=filter)

    filename = name[0]
    return filename


def get_directory():
    try:
        desktop_path = os.environ['USERPROFILE'] + '\Desktop\\'
        dir = str(QtWidgets.QFileDialog.getExistingDirectory(caption="Choisir un emplacement", directory=desktop_path))
    except:
        dir = str(QtWidgets.QFileDialog.getExistingDirectory(caption="Choisir un emplacement"))
    return dir

def create_radio_button(text):
    button = QtWidgets.QRadioButton()
    button.setText(text)
    return button


def create_button_group(widgets=None):
    group = QtWidgets.QButtonGroup()
    if widgets is not None:
        for index, widget in enumerate(widgets):
            group.addButton(widget, index)
    return group


def create_edit(text=None):
    edit = QtWidgets.QLineEdit()
    if text is not None:
        edit.setText(text)
    return edit
