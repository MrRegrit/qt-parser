import datetime
import sqlite3

import PyQt5.QtGui
import PyQt5.QtWidgets
import pyqtgraph as pg


class ItemDetailWidget(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, article):
        super().__init__()
        self.article = article
        self.item = self.get_item_prices(self.article)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("График изменения цены товара")
        self.setWindowIcon(PyQt5.QtGui.QIcon("static/icon.png"))
        price = [i[0] for i in self.item]
        date = [
            datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S.%f")
            for i in self.item
        ]

        date_axis = pg.DateAxisItem(orientation="bottom")

        self.plot_graph = pg.PlotWidget(axisItems={"bottom": date_axis})
        self.plot_graph.setBackground("w")
        pen = pg.mkPen(color=(255, 150, 150))
        self.plot_graph.plot(
            x=[x.timestamp() for x in date],
            y=price,
            pen=pen,
            symbol="o",
            symbolSize=5,
            symbolBrush="r",
        )
        self.plot_graph.setTitle(f"Товар: {self.article}")
        styles = {"font-size": "18px", "color": "grey"}
        self.plot_graph.setLabel("left", "Цена", **styles)
        self.plot_graph.setLabel("bottom", "Дата", **styles)
        self.plot_graph.showGrid(x=True, y=True)

        self.setCentralWidget(self.plot_graph)

    def get_item_prices(self, article):
        connection = sqlite3.connect("db.sqlite")
        cursor = connection.cursor()

        result = cursor.execute(
            "SELECT price, datetime FROM prices INNER JOIN items "
            "ON prices.item_id = items.id "
            f"WHERE article = {article} "
            "ORDER BY datetime",
        ).fetchall()

        connection.close()

        return result


__all__ = ["ItemDetailWidget"]
