import PyQt5.QtWidgets
import PyQt5.uic
import qt.select_window
import qt.all_articles_window


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parsers):
        super().__init__()

        self.parsers = parsers
        self.marketplaces = [i[0] for i in parsers]

        self.initUi()

    def initUi(self):
        PyQt5.uic.loadUi("qt/main.ui", self)
        self.load_article_btn.clicked.connect(self.open_select_window)
        self.get_articles_prices_btn.clicked.connect(
            self.open_all_articles_window
        )

    def open_select_window(self):
        self.select_window = qt.select_window.LoadNewArticleWidget(self)
        self.select_window.show()
        self.hide()

    def open_all_articles_window(self):
        self.all_articles_window = (
            qt.all_articles_window.LoadAllArticlesWidget(self)
        )
        self.all_articles_window.show()
        self.hide()
