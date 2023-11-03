import qt.main_window
import PyQt5.QtWidgets
import sys

parsers = (("wildberries", "parser_wb"),)


def start(parsers):
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = qt.main_window.MainWindow(parsers)
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start(parsers)
