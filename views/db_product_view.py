# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_product.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_db_product(object):
    def setupUi(self, db_product):
        db_product.setObjectName("db_product")
        db_product.resize(808, 426)
        self.centralwidget = QtWidgets.QWidget(db_product)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setText("")
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_id.setObjectName("label_id")
        self.verticalLayout.addWidget(self.label_id)
        self.label_descr = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_descr.setFont(font)
        self.label_descr.setText("")
        self.label_descr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descr.setObjectName("label_descr")
        self.verticalLayout.addWidget(self.label_descr)
        self.label_download = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_download.setFont(font)
        self.label_download.setText("")
        self.label_download.setAlignment(QtCore.Qt.AlignCenter)
        self.label_download.setObjectName("label_download")
        self.verticalLayout.addWidget(self.label_download)
        self.edit_seq = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_seq.sizePolicy().hasHeightForWidth())
        self.edit_seq.setSizePolicy(sizePolicy)
        self.edit_seq.setFrameShape(QtWidgets.QFrame.Box)
        self.edit_seq.setFrameShadow(QtWidgets.QFrame.Plain)
        self.edit_seq.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.edit_seq.setReadOnly(True)
        self.edit_seq.setObjectName("edit_seq")
        self.verticalLayout.addWidget(self.edit_seq)
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_buttons.addItem(spacerItem)
        self.label_copy = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_copy.setFont(font)
        self.label_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_copy.setObjectName("label_copy")
        self.layout_buttons.addWidget(self.label_copy)
        self.label_analyse = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_analyse.setFont(font)
        self.label_analyse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_analyse.setObjectName("label_analyse")
        self.layout_buttons.addWidget(self.label_analyse)
        self.verticalLayout.addLayout(self.layout_buttons)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree_widget = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_widget.setMinimumSize(QtCore.QSize(431, 0))
        self.tree_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tree_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tree_widget.setObjectName("tree_widget")
        self.tree_widget.header().setVisible(False)
        self.tree_widget.header().setMinimumSectionSize(40)
        self.tree_widget.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tree_widget)
        self.layout_features = QtWidgets.QVBoxLayout()
        self.layout_features.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layout_features.setObjectName("layout_features")
        self.horizontalLayout.addLayout(self.layout_features)
        self.verticalLayout.addLayout(self.horizontalLayout)
        db_product.setCentralWidget(self.centralwidget)

        self.retranslateUi(db_product)
        self.tree_widget.doubleClicked['QModelIndex'].connect(self.tree_widget.expand)
        QtCore.QMetaObject.connectSlotsByName(db_product)

    def retranslateUi(self, db_product):
        _translate = QtCore.QCoreApplication.translate
        db_product.setWindowTitle(_translate("db_product", "MainWindow"))
        self.label_copy.setText(_translate("db_product", "Copier"))
        self.label_analyse.setText(_translate("db_product", "Analyser"))
        self.tree_widget.headerItem().setText(0, _translate("db_product", "1"))
        self.tree_widget.headerItem().setText(1, _translate("db_product", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_product = QtWidgets.QMainWindow()
    ui = Ui_db_product()
    ui.setupUi(db_product)
    db_product.show()
    sys.exit(app.exec_())
