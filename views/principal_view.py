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
        Principal_Window.resize(402, 274)
        self.centralwidget = QtWidgets.QWidget(Principal_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.button_ncbi = QtWidgets.QPushButton(self.centralwidget)
        self.button_ncbi.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_ncbi.setFont(font)
        self.button_ncbi.setObjectName("button_ncbi")
        self.verticalLayout.addWidget(self.button_ncbi)
        self.button_db = QtWidgets.QPushButton(self.centralwidget)
        self.button_db.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_db.setFont(font)
        self.button_db.setObjectName("button_db")
        self.verticalLayout.addWidget(self.button_db)
        self.button_analyse = QtWidgets.QPushButton(self.centralwidget)
        self.button_analyse.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_analyse.setFont(font)
        self.button_analyse.setObjectName("button_analyse")
        self.verticalLayout.addWidget(self.button_analyse)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_connex_internet = QtWidgets.QLabel(self.centralwidget)
        self.label_connex_internet.setText("")
        self.label_connex_internet.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_connex_internet.setObjectName("label_connex_internet")
        self.horizontalLayout.addWidget(self.label_connex_internet)
        self.label_connex_db = QtWidgets.QLabel(self.centralwidget)
        self.label_connex_db.setText("")
        self.label_connex_db.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_connex_db.setObjectName("label_connex_db")
        self.horizontalLayout.addWidget(self.label_connex_db)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Principal_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal_Window)
        self.button_ncbi.clicked.connect(Principal_Window.button_ncbi_clicked)
        self.button_db.clicked.connect(Principal_Window.button_db_clicked)
        self.button_analyse.clicked.connect(Principal_Window.button_analyses_clicked)
        QtCore.QMetaObject.connectSlotsByName(Principal_Window)

    def retranslateUi(self, Principal_Window):
        _translate = QtCore.QCoreApplication.translate
        Principal_Window.setWindowTitle(_translate("Principal_Window", "MainWindow"))
        self.label_title.setText(_translate("Principal_Window", "SeqMining"))
        self.button_ncbi.setText(_translate("Principal_Window", "Accéder à NCBI Nucleotide en ligne"))
        self.button_db.setText(_translate("Principal_Window", "Accéder aux données de la base de données"))
        self.button_analyse.setText(_translate("Principal_Window", "Analyses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal_Window = QtWidgets.QMainWindow()
    ui = Ui_Principal_Window()
    ui.setupUi(Principal_Window)
    Principal_Window.show()
    sys.exit(app.exec_())
