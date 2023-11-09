import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class Ui_ShowDetailItem(object):
    def setupUi(self, ShowDetailItem):
        ShowDetailItem.setObjectName("ShowDetailItem")
        ShowDetailItem.resize(330, 74)
        ShowDetailItem.setWindowIcon(PyQt5.QtGui.QIcon("static/icon.png"))
        self.box_articles = PyQt5.QtWidgets.QComboBox(ShowDetailItem)
        self.box_articles.setGeometry(PyQt5.QtCore.QRect(10, 10, 311, 20))
        self.box_articles.setObjectName("box_articles")
        self.show_btn = PyQt5.QtWidgets.QPushButton(ShowDetailItem)
        self.show_btn.setGeometry(PyQt5.QtCore.QRect(10, 40, 151, 25))
        self.show_btn.setObjectName("show_btn")
        self.cancel_btn = PyQt5.QtWidgets.QPushButton(ShowDetailItem)
        self.cancel_btn.setGeometry(PyQt5.QtCore.QRect(170, 40, 151, 25))
        self.cancel_btn.setObjectName("cancel_btn")
        self.setFixedSize(330, 74)

        self.retranslateUi(ShowDetailItem)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(ShowDetailItem)

    def retranslateUi(self, ShowDetailItem):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        ShowDetailItem.setWindowTitle(
            _translate("ShowDetailItem", "Выберете товар"),
        )
        self.show_btn.setText(_translate("ShowDetailItem", "Открыть"))
        self.cancel_btn.setText(_translate("ShowDetailItem", "Отменить"))


__all__ = ["Ui_ShowDetailItem"]
