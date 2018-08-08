# misc.py

from iso_app.utils import db_parser


def create_button_list():
    """
    Create a beautiful button list and src list for jinja2 (Who need requests?)
    :return: dictionary with all information
    """
    button_dict = {}
    src_list = [999]
    for src in db_parser.get_attributes('src'):
        src_list.append(src)

    for spam in src_list:
        button_dict[spam] = db_parser.get_all(spam)

    return button_dict


def get_data(value):
    """
    Only to reduce imports in routes.py
    """
    return db_parser.get_all(int(value))
