import sqlite3

import PyQt5.QtWidgets

import qt.item_detail_window
import qt.select_to_detail_ui


class SelectItemToDetail(
    PyQt5.QtWidgets.QWidget,
    qt.select_to_detail_ui.Ui_ShowDetailItem,
):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.initUi()

    def initUi(self):
        self.setGeometry(self.main.geometry())
        self.setupUi(self)

        self.show_btn.clicked.connect(self.open_item_detail_window)
        self.cancel_btn.clicked.connect(self.close)

        self.items = self.get_items()
        self.box_articles.addItems([i[1] for i in self.items])

    def open_item_detail_window(self):
        selected_item_index = self.box_articles.currentIndex()
        self.item_detail_window = qt.item_detail_window.ItemDetailWidget(
            self.items[selected_item_index][0],
        )
        self.item_detail_window.show()

    @staticmethod
    def get_items():
        connection = sqlite3.connect("db.sqlite")
        cursor = connection.cursor()

        result = cursor.execute(
            "SELECT article, description FROM items",
        ).fetchall()

        connection.close()

        for num, art_and_descr in enumerate(result):
            article, description = art_and_descr
            if description == "":
                result[num] = (article, article)

        return result

    def closeEvent(self, event):
        self.main.setGeometry(self.geometry())
        self.main.show()
        event.accept()


__all__ = ["SelectItemToDetail"]
