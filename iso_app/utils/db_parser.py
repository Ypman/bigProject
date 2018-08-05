# db_parser.py

from iso_app.utils.iso import ISO


def get_color_values(source_id: int):
    if source_id == 999:
        result_dict = get_db_dict(source_id)
    else:
        result_dict = get_db_dict(source_id, False)
    new_dict = {}
    """
    for a new v(n) just copy&paste a elif statement and exchange for example 'v3' with 'v4'
    """
    for f in result_dict:
        if f['iso2'] not in new_dict:
            new_dict[f['iso2']] = {'v1': f['v1'], 'v2': f['v2'], 'v3': f['v3']}
        if f['v1'] > new_dict[f['iso2']]['v1']:
            new_dict[f['iso2']]['v1'] = f['v1']
        elif f['v2'] > new_dict[f['iso2']]['v2']:
            new_dict[f['iso2']]['v2'] = f['v2']
        elif f['v3'] > new_dict[f['iso2']]['v3']:
            new_dict[f['iso2']]['v3'] = f['v3']
    return new_dict


def get_db_dict(source_id, all_entrys=True):
    result_dict = []
    if all_entrys:
        for u in ISO.query.all():
            result_dict.append(u.__dict__)
    else:
        for u in ISO.query.filter_by(src=source_id).all():
            result_dict.append(u.__dict__)
    return result_dict


def get_description():
    source_id = 999
    result_dict = get_db_dict(source_id)

