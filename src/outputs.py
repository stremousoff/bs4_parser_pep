import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, Literals, PathConstants, UtilsConstants


def default_output(results, *args):
    for row in results:
        print(*row)


def pretty_output(results, *args):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args, encoding='utf-8'):
    results_dir = BASE_DIR / PathConstants.RESULTS_DIR
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now_formatted = dt.datetime.now().strftime(UtilsConstants.DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding=encoding) as file:
        csv.writer(file, dialect=csv.excel).writerows(results)
    logging.info(Literals.FILE_SAVED.format(file_path, file_name))


OUTPUT_PARAMS = {
    UtilsConstants.PRETTY: pretty_output,
    UtilsConstants.FILE: file_output,
    None: default_output
}


def control_output(results, cli_args):
    OUTPUT_PARAMS.get(cli_args.output)(results, cli_args)
