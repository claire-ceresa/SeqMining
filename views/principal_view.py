# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal_Window(object):
    def setupUi(self, Principal_Window):
        Principal_Window.setObjectName("Principal_Window")
        Principal_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Principal_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.button_ncbi = QtWidgets.QPushButton(self.centralwidget)
        self.button_ncbi.setObjectName("button_ncbi")
        self.verticalLayout.addWidget(self.button_ncbi)
        spacerItem = QtWidgets.QSpacerItem(20, 531, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        Principal_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal_Window)
        self.button_ncbi.clicked.connect(Principal_Window.button_ncbi_clicked)
        QtCore.QMetaObject.connectSlotsByName(Principal_Window)

    def retranslateUi(self, Principal_Window):
        _translate = QtCore.QCoreApplication.translate
        Principal_Window.setWindowTitle(_translate("Principal_Window", "MainWindow"))
        self.label_title.setText(_translate("Principal_Window", "SeqMining"))
        self.button_ncbi.setText(_translate("Principal_Window", "Accéder à NCBI Nucleotide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal_Window = QtWidgets.QMainWindow()
    ui = Ui_Principal_Window()
    ui.setupUi(Principal_Window)
    Principal_Window.show()
    sys.exit(app.exec_())
