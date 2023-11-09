import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class Ui_AddItem(object):
    def setupUi(self, AddItem):
        AddItem.setObjectName("AddItem")
        AddItem.resize(330, 135)
        AddItem.setFixedSize(330, 135)
        AddItem.setWindowIcon(PyQt5.QtGui.QIcon("static/icon.png"))
        self.line_article = PyQt5.QtWidgets.QLineEdit(AddItem)
        self.line_article.setGeometry(PyQt5.QtCore.QRect(10, 10, 150, 20))
        self.line_article.setText("")
        self.line_article.setObjectName("line_article")
        self.box_marketplaces = PyQt5.QtWidgets.QComboBox(AddItem)
        self.box_marketplaces.setGeometry(PyQt5.QtCore.QRect(170, 10, 150, 20))
        self.box_marketplaces.setObjectName("box_marketplaces")
        self.add_btn = PyQt5.QtWidgets.QPushButton(AddItem)
        self.add_btn.setGeometry(PyQt5.QtCore.QRect(10, 100, 151, 25))
        self.add_btn.setObjectName("add_btn")
        self.cancel_btn = PyQt5.QtWidgets.QPushButton(AddItem)
        self.cancel_btn.setGeometry(PyQt5.QtCore.QRect(170, 100, 151, 25))
        self.cancel_btn.setObjectName("cancel_btn")
        self.line_description = PyQt5.QtWidgets.QLineEdit(AddItem)
        self.line_description.setGeometry(PyQt5.QtCore.QRect(10, 60, 311, 20))
        self.line_description.setWhatsThis("")
        self.line_description.setAccessibleName("")
        self.line_description.setAccessibleDescription("")
        self.line_description.setObjectName("line_description")
        self.error_label = PyQt5.QtWidgets.QLabel(AddItem)
        self.error_label.setGeometry(PyQt5.QtCore.QRect(10, 40, 301, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(AddItem)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(AddItem)

    def retranslateUi(self, AddItem):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        AddItem.setWindowTitle(_translate("AddItem", "Добавление товара"))
        self.line_article.setPlaceholderText(
            _translate("AddItem", "Введите артикул"),
        )
        self.add_btn.setText(_translate("AddItem", "Добавить"))
        self.cancel_btn.setText(_translate("AddItem", "Отменить"))
        self.line_description.setPlaceholderText(
            _translate("AddItem", "Добавте предписание"),
        )


__all__ = ["Ui_AddItem"]
