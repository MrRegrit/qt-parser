import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 300)
        Form.setWindowIcon(PyQt5.QtGui.QIcon("static/icon.png"))
        Form.setAutoFillBackground(False)
        self.gridLayout = PyQt5.QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.table = PyQt5.QtWidgets.QTableWidget(Form)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.retranslateUi(Form)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Данные о товарах"))


__all__ = ["Ui_Form"]
