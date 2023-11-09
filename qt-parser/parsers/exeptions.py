class ArticleError(Exception):
    pass


class InvalidArticle(ArticleError):
    pass


class Article404(ArticleError):
    pass


__all__ = ["InvalidArticle", "Article404"]
