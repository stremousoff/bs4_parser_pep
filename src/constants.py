from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_MAIN_URL = 'https://peps.python.org/'
BASE_DIR = Path(__file__).parent

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}


class UtilsConstants:
    PRETTY = 'pretty'
    FILE = 'file'
    DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
    DT_FORMAT = '%d.%m.%Y %H:%M:%S'
    LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'


class PathConstants:
    RESULTS_DIR = 'results'
    DOWNLOADS_DIR = 'downloads'
    PARSER_LOG_DIR = 'logs'
    NAME_PARSER_FILE = 'parser.log'



class Literals:
    CONNECTION_ERROR = 'Возникла ошибка при загрузке страницы {}: {}.'
    TAG_NOT_FIND_ERROR = 'Не найден тег {} {}.'
    FILE_SAVED = 'Файл с результатами был сохранён {}/{}.'
    HTTP_RESPONSE_ERROR = 'Не получилось получить данные от {}, причина {}.'
    NOT_FIND_LIST_VERSIONS = 'Не найден список c версиями Python'
    ARCHIVE_SAVED = 'Архив(имя {}) был сохранён по адресу {}.'
    MISMATCHING_STATUS = ('Статус {} не соответствует ожидаемому: {}. Статус '
                          'взят со страницы - {}')
    PARSER_START = 'Парсер запущен.'
    ARGUMENTS_COMMAND = 'Следующие аргументы командной строки: {}'
    PARSER_FINISH = 'Парсер данных завершен.'
    PARSER_EXCEPTION = 'Возникла ошибка: {}.'
