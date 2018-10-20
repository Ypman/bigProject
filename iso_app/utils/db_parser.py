# db_parser.py

from iso_app.utils.iso import ISO


def get_all(source_id):
    result_list = []
    iso_counter = []
    if source_id == 999:
        for i in get_iso(source_id):
            if i.iso2 not in iso_counter:
                result_list.append({'id': i.iso2,
                                    'color': color_picker(get_xored_color(i.iso2)),
                                    'description': str(create_desc(i.iso2))
                                    })
                iso_counter.append(i.iso2)
    else:
        for i in get_iso(source_id, False):
            if i.iso2 not in iso_counter:
                result_list.append({'id': i.iso2,
                                    'color': color_picker(get_xored_color(i.iso2, source_id)),
                                    'description': str(create_desc(i.iso2))
                                    })
                iso_counter.append(i.iso2)

        for entry in get_iso(999):
            if entry.iso2 not in iso_counter:
                # print(entry.iso2, 'blubb')
                result_list.append({'id': entry.iso2,
                                    'color': '#555555',
                                    'description': str(create_desc(entry.iso2))
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
        for l in ISO.query.all():
            temp_dict = l.__dict__
            if temp_dict[attribute] not in attribute_list:
                attribute_list.append(temp_dict[attribute])
    else:
        for l in ISO.query.filter_by(iso2=iso).all():
            temp_dict = l.__dict__
            if temp_dict[attribute] not in attribute_list:
                attribute_list.append(temp_dict[attribute])
    return attribute_list


def color_picker(value_dict):
    color_helper_dict = {
        'v1': {0: '55', 1: '99'},
        'v2': {0: '55', 1: '99'},
        'v3': {0: '55', 1: '99'}
    }
    return '#{}{}{}'.format(color_helper_dict['v1'][value_dict['v1']],
                            color_helper_dict['v2'][value_dict['v2']],
                            color_helper_dict['v3'][value_dict['v3']])


def get_xored_color(iso, source_id=None):
    """
    If there is a value v4 in future given you need to add this here
    :param iso: given iso
    :param source_id: specialized by source
    :return: a complete color dict for specific iso
    """
    if source_id is None:
        return xor(ISO.query.filter_by(iso2=iso))
    else:
        return xor(ISO.query.filter_by(iso2=iso, src=source_id))


def xor(db_result):
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
    # TODO rename attributes!
    attribute_list = ['hakuna', 'matata', 'province', 'src', 'v1', 'v2', 'v3']
    desc_dict = {}
    for attribute in attribute_list:
        desc_dict[attribute] = get_attributes(attribute, iso)

    new_string = ""
    for key, value in desc_dict.items():
        # new_string.join(key + ": " + str(value))
        # print(key, value)
        new_string = new_string + key + ": " + str(value) + "\n"
    return new_string


# src_list = desc_dict['src']
# value_list = []
# for i in src_list:
#      if 999 not in i:
#          value_list.append(xor(iso, i))
#      else:
#          append(xor(iso))     kann man auch weglassen

# new_string = 'hakuna: ' + str(desc_dict['hakuna']) + '\n' +
#                       'matata: ' + str(desc_dict['matata']) + '\n' +
#                       'province: ' + str(desc_dict['province']) + '\n'


print(get_iso(92))
