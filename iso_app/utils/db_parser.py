# db_parser.py

from iso_app.utils.iso import ISO


def get_all(source_id: int):
    if source_id == 999:
        result_dict = get_db_dict(source_id)
    else:
        result_dict = get_db_dict(source_id, False)

    """
    for a new v(n) just copy&paste a elif statement and exchange for example 'v3' with 'v4'
    """
    new_dict = xored_values(result_dict)
    color_dict = color_picker(new_dict)

    desc_dict = get_desc(get_db_dict(999))

    complete_dict = []
    for i in desc_dict:
        if i not in color_dict:
            temp_dict = {'id': i, 'color': '#555555', 'description': desc_dict[i]}
        else:
            temp_dict = {'id': i, 'color': color_dict[i], 'description': desc_dict[i]}
        complete_dict.append(temp_dict)

    return complete_dict


def color_picker(new_dict):
    color_helper_dict = {
        'v1': {0: '55', 1: '99'},
        'v2': {0: '55', 1: '99'},
        'v3': {0: '55', 1: '99'}
    }
    spam = {}
    for dd in new_dict:
        spam[dd] = '#{}{}{}'.format(
            color_helper_dict['v1'][new_dict[dd]['v1']],
            color_helper_dict['v2'][new_dict[dd]['v2']],
            color_helper_dict['v3'][new_dict[dd]['v3']])

    return spam


def xored_values(result_dict):
    new_dict = {}
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


def get_desc(result_dict):
    new_dict = {}
    for f in result_dict:
        if f['iso2'] not in new_dict:
            new_dict[f['iso2']] = {'hakuna': [f['hakuna']],
                                   'matata': [f['matata']],
                                   'province': [f['province']],
                                   'src': [f['src']]
                                   }
        else:
            if f['hakuna'] not in new_dict[f['iso2']]['hakuna']:
                new_dict[f['iso2']]['hakuna'].append(f['hakuna'])
            if f['matata'] not in new_dict[f['iso2']]['matata']:
                new_dict[f['iso2']]['matata'].append(f['matata'])
            if f['province'] not in new_dict[f['iso2']]['province']:
                new_dict[f['iso2']]['province'].append(f['province'])
            if f['src'] not in new_dict[f['iso2']]['src']:
                new_dict[f['iso2']]['src'].append(f['src'])

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
