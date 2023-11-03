import fake_useragent
import requests
import sqlite3
import parsers.exeptions

url_marketplace = "https://card.wb.ru/cards/v1/detail?curr=rub&nm="


def get_prices():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    items = cursor.execute(
        "SELECT id, article, description "
        "FROM items WHERE marketplace like 'wildberries'"
    ).fetchall()

    connection.close()

    ua = fake_useragent.UserAgent().random
    headers = {"User-Agent": ua}

    items_ids = [i[0] for i in items]
    items_articles = [i[1] for i in items]
    items_descriptions = [i[2] for i in items]

    url = url_marketplace + ";".join(items_articles)

    page = requests.get(url, headers=headers).json()

    result = []

    for num, product in enumerate(page["data"]["products"]):
        base = (items_ids[num], items_articles[num], items_descriptions[num])
        if "name" in product:
            result.append(
                base + (product["name"], product["salePriceU"] / 100)
            )
        else:
            result.append(
                base
                + (
                    "Проверьте актуальность артикула",
                    "Проверьте актуальность артикула",
                )
            )

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
