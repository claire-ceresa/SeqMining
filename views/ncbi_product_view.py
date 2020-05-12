# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ncbi_product.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NCBI_Product(object):
    def setupUi(self, NCBI_Product):
        NCBI_Product.setObjectName("NCBI_Product")
        NCBI_Product.resize(631, 620)
        self.centralwidget = QtWidgets.QWidget(NCBI_Product)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_dispo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dispo.setFont(font)
        self.label_dispo.setText("")
        self.label_dispo.setObjectName("label_dispo")
        self.horizontalLayout.addWidget(self.label_dispo)
        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setObjectName("button_download")
        self.horizontalLayout.addWidget(self.button_download)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        NCBI_Product.setCentralWidget(self.centralwidget)

        self.retranslateUi(NCBI_Product)
        self.button_download.clicked.connect(NCBI_Product.button_download_clicked)
        QtCore.QMetaObject.connectSlotsByName(NCBI_Product)

    def retranslateUi(self, NCBI_Product):
        _translate = QtCore.QCoreApplication.translate
        NCBI_Product.setWindowTitle(_translate("NCBI_Product", "MainWindow"))
        self.button_download.setText(_translate("NCBI_Product", "Télécharger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NCBI_Product = QtWidgets.QMainWindow()
    ui = Ui_NCBI_Product()
    ui.setupUi(NCBI_Product)
    NCBI_Product.show()
    sys.exit(app.exec_())
