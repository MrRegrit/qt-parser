import PyQt5.QtWidgets
import PyQt5.uic
import sqlite3
import importlib.util


class LoadNewArticleWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setGeometry(self.main.geometry())
        PyQt5.uic.loadUi("qt/select.ui", self)
        self.add_btn.clicked.connect(self.add_article)
        self.cancel_btn.clicked.connect(self.close)
        self.box_marketplaces.addItems(self.main.marketplaces)

    def add_article(self):
        selected_marketplace = self.box_marketplaces.currentText()
        for mp, path in self.main.parsers:
            if mp == selected_marketplace:
                try:
                    spec = importlib.util.spec_from_file_location(
                        path, "parsers/" + path + ".py"
                    )
                    parser = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(parser)
                    parser.try_connect(self.line_article.text())
                except Exception as exp:
                    self.error_label.setText(str(exp))
                else:
                    connection = sqlite3.connect("db.sqlite")
                    cursor = connection.cursor()
                    cursor.execute(
                        f"INSERT INTO "
                        f"items(article, marketplace, description) "
                        f"VALUES "
                        f"('{self.line_article.text()}', "
                        f"'{selected_marketplace}', "
                        f"'{self.line_description.text()}')"
                    )
                    connection.commit()
                    connection.close()
                    self.error_label.setText("")

    def closeEvent(self, event):
        self.main.setGeometry(self.geometry())
        self.main.show()
        event.accept()
