# db_parser.py

from flask import render_template

from iso_app.utils.iso import ISO


def get_all(source_id):
    result_list = []
    iso_counter = []
    if source_id == 999:
        for i in get_iso(source_id):
            if i.iso2 not in iso_counter:
                result_list.append({'id': i.iso2,
                                    'color': color_picker(get_ored_color(i.iso2)),
                                    'description': create_desc(i.iso2)
                                    })
                iso_counter.append(i.iso2)
    else:
        for i in get_iso(source_id, False):
            if i.iso2 not in iso_counter:
                result_list.append({'id': i.iso2,
                                    'color': color_picker(get_ored_color(i.iso2, source_id)),
                                    'description': create_desc(i.iso2)
                                    })
                iso_counter.append(i.iso2)

        for entry in get_iso(999):
            if entry.iso2 not in iso_counter:
                result_list.append({'id': entry.iso2,
                                    'color': '#555555',
                                    'description': create_desc(entry.iso2)
                                    })
                iso_counter.append(entry.iso2)

    return result_list


def get_iso(source_id, all=True):
    if all:
        return ISO.query.all()
    else:
        return ISO.query.filter_by(src=source_id).all()


def get_attributes(attribute, iso=None):
    attribute_list = []
    if iso is None:
        iterating_through_attributes(attribute, attribute_list, ISO.query.all())
    else:
        iterating_through_attributes(attribute, attribute_list, ISO.query.filter_by(iso2=iso).all())
    return attribute_list


def iterating_through_attributes(attribute, attribute_list, iso_query):
    for l in iso_query:
        temp_dict = l.__dict__
        if temp_dict[attribute] not in attribute_list:
            attribute_list.append(temp_dict[attribute])


def color_picker(value_dict):
    color_helper_dict = {
        'v1': {0: '55', 1: '99'},
        'v2': {0: '55', 1: '99'},
        'v3': {0: '55', 1: '99'}
    }
    return '#{}{}{}'.format(color_helper_dict['v1'][value_dict['v1']],
                            color_helper_dict['v2'][value_dict['v2']],
                            color_helper_dict['v3'][value_dict['v3']])


def get_ored_color(iso, source_id=None, matata=None):
    """
    If there is a value v4 in future given you need to add this here
    :param matata: specialized by matata
    :param iso: given iso
    :param source_id: specialized by source
    :return: a complete color dict for specific iso
    """
    if source_id is None and matata is None:
        return or_func(ISO.query.filter_by(iso2=iso))
    elif matata is None:
        return or_func(ISO.query.filter_by(iso2=iso, src=source_id))
    elif source_id is None:
        return or_func(ISO.query.filter_by(iso2=iso, matata=matata))


def or_func(db_result):
    temp = {'v1': 0, 'v2': 0, 'v3': 0}
    for ad in db_result:
        if ad.v1 > temp['v1'] and not None:
            temp['v1'] = ad.v1
        if ad.v2 > temp['v2'] and not None:
            temp['v2'] = ad.v2
        if ad.v3 > temp['v3'] and not None:
            temp['v3'] = ad.v3
    return temp


def create_desc(iso):
    src_query = ISO.query.filter_by(iso2=iso)
    desc_dict = None

    for sources in src_query:
        temp_src_query = ISO.query.filter_by(iso2=iso, src=sources.src)
        for kp in temp_src_query:
            if not desc_dict:
                desc_dict = {kp.hakuna: {kp.matata: [kp.v1, kp.v2, kp.v3, kp.src]}}
            elif kp.hakuna in desc_dict and kp.matata not in desc_dict[kp.hakuna]:
                desc_dict[kp.hakuna][kp.matata] = [kp.v1, kp.v2, kp.v3, kp.src]
            elif kp.hakuna not in desc_dict:
                desc_dict[kp.hakuna] = {kp.matata: [kp.v1, kp.v2, kp.v3, kp.src]}

    return render_template("desc.html", desc_dict=desc_dict)
