import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 107)
        MainWindow.setMinimumSize(PyQt5.QtCore.QSize(241, 107))
        MainWindow.setMaximumSize(PyQt5.QtCore.QSize(241, 107))
        MainWindow.setWindowIcon(PyQt5.QtGui.QIcon("static/icon.png"))
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_article_btn = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.load_article_btn.setGeometry(PyQt5.QtCore.QRect(10, 10, 221, 23))
        self.load_article_btn.setObjectName("load_article_btn")
        self.get_articles_prices_btn = PyQt5.QtWidgets.QPushButton(
            self.centralwidget,
        )
        self.get_articles_prices_btn.setGeometry(
            PyQt5.QtCore.QRect(10, 40, 221, 23),
        )
        self.get_articles_prices_btn.setObjectName("get_articles_prices_btn")
        self.open_graphic_item_btn = PyQt5.QtWidgets.QPushButton(
            self.centralwidget,
        )
        self.open_graphic_item_btn.setGeometry(
            PyQt5.QtCore.QRect(10, 70, 221, 23),
        )
        self.open_graphic_item_btn.setObjectName("open_graphic_item_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Менеджер"))
        self.load_article_btn.setText(
            _translate("MainWindow", "Загрузить новый артикул"),
        )
        self.get_articles_prices_btn.setText(
            _translate("MainWindow", "Получить все актуальные данные"),
        )
        self.open_graphic_item_btn.setText(
            _translate("MainWindow", "Открыть график цен товара"),
        )


__all__ = ["Ui_MainWindow"]
