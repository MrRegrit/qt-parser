import importlib.util
import sqlite3

import PyQt5.QtWidgets

import qt.load_new_item_ui


class LoadNewItemWidget(
    PyQt5.QtWidgets.QWidget,
    qt.load_new_item_ui.Ui_AddItem,
):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.initUi()

    def initUi(self):
        self.setGeometry(self.main.geometry())
        self.setupUi(self)

        self.add_btn.clicked.connect(self.add_item)
        self.cancel_btn.clicked.connect(self.close)
        self.box_marketplaces.addItems(self.main.marketplaces)

    def add_item(self):
        item_article = self.line_article.text()
        selected_marketplace = self.box_marketplaces.currentText()
        item_description = self.line_description.text()

        for marketplace, path in self.main.parsers:
            if marketplace == selected_marketplace:
                try:
                    self.try_check_data(path, item_article)
                except Exception as exp:
                    self.error_label.setText(str(exp))
                else:
                    self.add_item_to_sql(
                        item_article,
                        selected_marketplace,
                        item_description,
                    )
                    self.error_label.setText("Артикул успешно добавлен в базу")

    @staticmethod
    def try_check_data(path, article):
        spec = importlib.util.spec_from_file_location(
            path,
            "parsers/" + path + ".py",
        )
        parser = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(parser)
        parser.check_data(article)

    @staticmethod
    def add_item_to_sql(article, marketplace, description):
        connection = sqlite3.connect("db.sqlite")

        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO "
            f"items(article, marketplace, description) "
            f"VALUES "
            f"('{article}', "
            f"'{marketplace}', "
            f"'{description}')",
        )

        connection.commit()
        connection.close()

    def closeEvent(self, event):
        self.main.setGeometry(self.geometry())
        self.main.show()
        event.accept()


__all__ = ["LoadNewItemWidget"]
