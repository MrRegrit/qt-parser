import PyQt5.QtWidgets
import PyQt5.uic
import importlib.util
import sqlite3
import datetime


class LoadAllArticlesWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setGeometry(self.main.geometry())
        self.initUi()

    def initUi(self):
        PyQt5.uic.loadUi("qt/all_articles.ui", self)
        all_prices = []
        for mp, path in self.main.parsers:
            spec = importlib.util.spec_from_file_location(
                path, "parsers/" + path + ".py"
            )
            parser = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(parser)
            items = parser.get_prices()
            for item in items:
                all_prices.append(item[1:])
                if item[-1] != "Проверьте актуальность артикула":
                    connection = sqlite3.connect("db.sqlite")
                    cursor = connection.cursor()
                    print(item[0], item[-1], datetime.datetime.now())
                    cursor.execute(
                        f"INSERT INTO "
                        f"prices(item_id, price, datetime) "
                        f"VALUES "
                        f"('{item[0]}', "
                        f"{item[-1]}, "
                        f"'{datetime.datetime.now()}')"
                    )
                    connection.commit()
                    connection.close()

        self.table.setRowCount(len(all_prices))
        self.table.setColumnCount(4)
        for y, item in enumerate(all_prices):
            for x, table_item in enumerate(item):
                self.table.setItem(
                    y, x, PyQt5.QtWidgets.QTableWidgetItem(str(table_item))
                )
        self.table.resizeColumnsToContents()

    def closeEvent(self, event):
        self.main.setGeometry(self.geometry())
        self.main.show()
        event.accept()
