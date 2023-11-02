import PyQt5.QtWidgets
import PyQt5.uic
import sqlite3
import sys
import importlib.util


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, parsers):
        super().__init__()
        self.parsers = parsers
        self.marketplaces = [i[0] for i in parsers]
        PyQt5.uic.loadUi("qt/main.ui", self)
        self.load_article_btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = LoadNewArticleWidget(self)
        self.second_form.show()
        self.hide()


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


def start(parsers):
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MainWindow(parsers)
    ex.show()
    sys.exit(app.exec())
