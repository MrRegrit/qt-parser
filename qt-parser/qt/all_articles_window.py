import datetime
import importlib.util
import sqlite3

import PyQt5.QtWidgets

import qt.all_articles_ui


class LoadAllArticlesWidget(
    PyQt5.QtWidgets.QWidget,
    qt.all_articles_ui.Ui_Form,
):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.initUi()

    def initUi(self):
        self.setGeometry(self.main.geometry())
        self.setupUi(self)

        items = self.get_items()
        self.set_items_to_table(items)
        self.add_items_prices_to_sql(items)

    def get_items(self):
        for mp, path in self.main.parsers:
            spec = importlib.util.spec_from_file_location(
                path,
                "parsers/" + path + ".py",
            )
            parser = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(parser)
        return parser.parsing_items()

    def set_items_to_table(self, items):
        all_prices = []
        for item in items:
            all_prices.append(item[1:])

        self.table.setRowCount(len(all_prices))
        self.table.setColumnCount(4)

        for y, item in enumerate(all_prices):
            for x, table_item in enumerate(item):
                self.table.setItem(
                    y,
                    x,
                    PyQt5.QtWidgets.QTableWidgetItem(str(table_item)),
                )

        self.table.resizeColumnsToContents()
        self.table.setHorizontalHeaderLabels(
            ["Артикул", "Ваше описание", "Имя", "Цена"],
        )

    @staticmethod
    def add_items_prices_to_sql(items):
        if len(items) == 0:
            return

        sql_response = "INSERT INTO prices(item_id, price, datetime) VALUES "

        for item in items:
            if type(item[-1]) is int or type(item[-1]) is float:
                sql_response += (
                    f"({item[0]}, {item[-1]}, '{datetime.datetime.now()}'), "
                )

        sql_response = sql_response[:-2]

        connection = sqlite3.connect("db.sqlite")
        cursor = connection.cursor()
        if len(sql_response) > 52:
            cursor.execute(sql_response)

        connection.commit()
        connection.close()

    def closeEvent(self, event):
        self.main.resize(self.size())
        self.main.show()
        event.accept()


__all__ = ["LoadAllArticlesWidget"]
