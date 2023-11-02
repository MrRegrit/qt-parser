import fake_useragent
import requests
import sqlite3
import parsers.exeptions

url_marketplace = "https://card.wb.ru/cards/v1/detail?curr=rub&nm="


def get_prices():
    connection = sqlite3.connect("../db.sqlite")
    cursor = connection.cursor()

    items_articles = cursor.execute(
        """SELECT article FROM items WHERE marketplace like 'wildberries'"""
    ).fetchall()

    ua = fake_useragent.UserAgent().random
    headers = {"User-Agent": ua}

    items_articles = [i[0] for i in items_articles]

    url = url_marketplace + ";".join(items_articles)

    page = requests.get(url, headers=headers).json()

    result = []

    for product in page["data"]["products"]:
        result.append(product["salePriceU"] / 100)

    connection.close()

    return result


def try_connect(article):
    ua = fake_useragent.UserAgent().random
    headers = {"User-Agent": ua}
    url = url_marketplace + article
    if not article.isdigit():
        raise parsers.exeptions.InvalidArticle(
            "Артикул для вб должен состоять только из цифр"
        )
    page = requests.get(url, headers=headers).json()
    if not page["data"]["products"]:
        raise parsers.exeptions.Article404(
            "Данные о товаре не получены. Проверьте артикул"
        )
