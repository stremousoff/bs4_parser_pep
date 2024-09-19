class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""


class ConnectionErrorException(Exception):
    """Вызывается, когда парсер не может получить доступ к сайту."""
