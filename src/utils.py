import logging
from http import HTTPStatus

from bs4 import BeautifulSoup
from requests import RequestException

from constants import Literals
from exceptions import ConnectionErrorException, ParserFindTagException


def get_response(session, url, encoding='utf-8'):
    try:
        response = session.get(url)
        response.encoding = encoding
        if response.status_code != HTTPStatus.OK:
            logging.info(
                Literals.HTTP_RESPONSE_ERROR.format(url, response.status_code)
            )
        return response
    except RequestException as error:
        raise ConnectionErrorException(
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
