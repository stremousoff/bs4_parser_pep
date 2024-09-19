import logging

from bs4 import BeautifulSoup
from requests import RequestException

from constants import Literals
from exceptions import ParserFindTagException


def get_response(session, url, encoding='utf-8'):
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException as error:
        raise ConnectionError(
            Literals.CONNECTION_ERROR.format(url, error)
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=attrs if attrs is not None else {})
    if searched_tag is None:
        raise ParserFindTagException(
            Literals.TAG_NOT_FIND_ERROR.format(tag, attrs)
        )
    return searched_tag


def make_soup(session, url, features='lxml'):
    return BeautifulSoup(get_response(session, url).text, features)


def check_exceptions(exceptions):
    list(map(lambda exception: logging.error(exception), exceptions))
