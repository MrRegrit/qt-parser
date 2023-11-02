class ArticleError(Exception):
    pass


class InvalidArticle(ArticleError):
    pass


class Article404(ArticleError):
    pass
