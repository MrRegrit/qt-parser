import PyQt5.QtWidgets

import qt.all_articles_window
import qt.load_new_item_window
import qt.main_ui
import qt.select_to_detail_window


class MainWindow(PyQt5.QtWidgets.QMainWindow, qt.main_ui.Ui_MainWindow):
    def __init__(self, parsers):
        super().__init__()

        self.parsers = parsers
        self.marketplaces = [i[0] for i in parsers]

        self.initUi()

    def initUi(self):
        self.setupUi(self)

        self.load_article_btn.clicked.connect(self.open_load_new_item_window)
        self.get_articles_prices_btn.clicked.connect(
            self.open_all_articles_window,
        )
        self.open_graphic_item_btn.clicked.connect(
            self.open_select_to_detail_window,
        )

    def open_load_new_item_window(self):
        self.load_new_item_window = qt.load_new_item_window.LoadNewItemWidget(
            self,
        )
        self.load_new_item_window.show()
        self.hide()

    def open_all_articles_window(self):
        self.all_articles_window = (
            qt.all_articles_window.LoadAllArticlesWidget(self)
        )
        self.all_articles_window.show()
        self.hide()

    def open_select_to_detail_window(self):
        self.select_to_detail_window = (
            qt.select_to_detail_window.SelectItemToDetail(self)
        )
        self.select_to_detail_window.show()
        self.hide()


__all__ = ["MainWindow"]
