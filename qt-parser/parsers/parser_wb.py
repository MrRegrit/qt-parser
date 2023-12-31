import sqlite3

import requests

import parsers.exeptions

url_marketplace = "https://card.wb.ru/cards/v1/detail?curr=rub&nm="


def get_items_from_sql():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    result = cursor.execute(
        "SELECT id, article, description "
        "FROM items WHERE marketplace like 'wildberries'",
    ).fetchall()

    connection.close()

    return result


def get_page(articles):

    url = url_marketplace + ";".join(articles)

    return requests.get(url).json()


def parsing_items():
    items = get_items_from_sql()

    items_ids = [i[0] for i in items]
    items_articles = [i[1] for i in items]
    items_descriptions = [i[2] for i in items]

    request_json = get_page(items_articles)

    result = []

    for num, product in enumerate(request_json["data"]["products"]):
        base = (items_ids[num], items_articles[num], items_descriptions[num])
        if "name" in product:
            result.append(
                (*base, product["name"], product["salePriceU"] / 100),
            )
        else:
            result.append(
                (
                    *base,
                    "Проверьте актуальность артикула",
                    "Проверьте актуальность артикула",
                ),
            )

    return result


def check_data(article):
    url = url_marketplace + article

    if not article.isdigit():
        raise parsers.exeptions.InvalidArticle(
            "Артикул для вб должен состоять только из цифр",
        )

    page = requests.get(url).json()

    if not page["data"]["products"]:
        raise parsers.exeptions.Article404(
            "Данные о товаре не получены. Проверьте артикул",
        )


__all__ = ["check_data", "parsing_items"]
