import logging
import re
from collections import defaultdict
from urllib.parse import urljoin

import requests_cache
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (BASE_DIR, EXPECTED_STATUS, MAIN_DOC_URL, PEP_MAIN_URL,
                       Literals, PathConstants)
from outputs import control_output
from utils import check_exceptions, find_tag, make_soup


def whats_new(session):
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    results = [('Ссылка на статью', 'Заголовок', 'Редактор, автор')]
    exceptions = []
    for version_a_tag in tqdm(
        make_soup(session, whats_new_url).select(
            '#what-s-new-in-python div.toctree-wrapper li.toctree-l1 > a'
        )[:-1]
    ):
        version_link = urljoin(whats_new_url, version_a_tag['href'])
        try:
            soup = make_soup(session, version_link)
        except ConnectionError as error:
            exceptions.append(
                Literals.CONNECTION_ERROR.format(version_link, error)
            )
            continue
        results.append(
            (
                version_link,
                find_tag(soup, 'h1').text.replace('¶', ''),
                find_tag(soup, 'dl').text.replace('\n', ' '))
        )
    check_exceptions(exceptions)
    return results


def latest_versions(session):
    soup = make_soup(session, MAIN_DOC_URL)
    ul_tags = soup.select('div.sphinxsidebarwrapper > ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise RuntimeError(Literals.NOT_FIND_LIST_VERSIONS)

    results = [('Ссылка на документацию', 'Версия', 'Статус')]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in a_tags:
        text_match = re.search(pattern, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append((a_tag['href'], version, status))
    return results


def download(session):
    pdf_a4_link = make_soup(
        session,
        urljoin(MAIN_DOC_URL, 'download.html')
    ).select_one('div.body > table.docutils a[href$="pdf-a4.zip"]')['href']
    archive_url = urljoin(MAIN_DOC_URL, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / PathConstants.DOWNLOADS_DIR
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    response = session.get(archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(Literals.ARCHIVE_SAVED.format(filename, archive_path))


def pep(session):
    soup = make_soup(session, PEP_MAIN_URL)
    rows = soup.select(
        'section#numerical-index '
        '.pep-zero-table.docutils.align-default '
        'tr'
    )
    result = defaultdict(int)
    mismatches, exceptions = [], []
    for row in tqdm(rows[1:]):
        status = row.select_one('abbr').text[1:]
        url = urljoin(PEP_MAIN_URL, row.select_one('a').get('href'))
        try:
            soup = make_soup(session, url)
        except ConnectionError as error:
            exceptions.append(Literals.CONNECTION_ERROR.format(url, error))
            continue
        page_status = soup.select_one('#pep-content > dl abbr').text
        if page_status not in EXPECTED_STATUS[status]:
            mismatches.append(
                Literals.MISMATCHING_STATUS.format(
                    page_status, EXPECTED_STATUS[status], url
                )
            )
            continue
        result[page_status] += 1
    if mismatches:
        logging.info('\n'.join(mismatches))
    check_exceptions(exceptions)
    return [
        ('Status', 'Count'),
        *sorted(result.items()),
        ('Total:', sum(result.values())),
    ]


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep,
}


def main():
    try:
        configure_logging()
        logging.info(Literals.PARSER_START)
        arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
        args = arg_parser.parse_args()
        logging.info(Literals.ARGUMENTS_COMMAND.format(args))
        session = requests_cache.CachedSession()
        if args.clear_cache:
            session.cache.clear()
        parser_mode = args.mode
        results = MODE_TO_FUNCTION[parser_mode](session)
        if results is not None:
            control_output(results, args)
        logging.info(Literals.PARSER_FINISH)
    except Exception as error:
        logging.exception(Literals.PARSER_EXCEPTION.format(error))


if __name__ == '__main__':
    main()
