import sqlite3
import sys

import PyQt5.QtWidgets

import qt.main_window

parsers = (("wildberries", "parser_wb"),)


def start(parsers):
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = qt.main_window.MainWindow(parsers)
    ex.show()
    sys.exit(app.exec())


def createdb():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    cursor.execute(
        "create table items"
        "(id INTEGER primary key autoincrement, "
        "article  TEXT not null, "
        "marketplace TEXT not null, "
        "description TEXT)",
    ).fetchall()
    cursor.execute(
        "create table prices"
        "(id INTEGER primary key autoincrement, "
        "item_id  INTEGER not null references items, "
        "price INTEGER not null, "
        "datetime TEXT)",
    ).fetchall()
    connection.commit()
    connection.close()


if __name__ == "__main__":
    argv = sys.argv
    if sys.argv[1] == "start":
        start(parsers)
    elif sys.argv[1] == "createdb":
        createdb()
    else:
        raise ValueError("Введите createdb or start")

__all__ = []
