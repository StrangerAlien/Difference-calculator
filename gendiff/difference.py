from gendiff.parse_file import get_data


def get_diff(data1, data2):

    differ = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in keys:
        if key not in data1.keys():
            differ.append({
                'key': key,
                'type': 'add',
                'value': data2[key]
            })
        elif key not in data2.keys():
            differ.append({
                'key': key,
                'type': 'remove',
                'value': data1[key]
            })
        elif isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
            differ.append({
                'key': key,
                'type': 'children',
                'value': get_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            differ.append({
                'key': key,
                'type': 'same',
                'value': data1[key]
            })
        else:
            differ.append({
                'key': key,
                'type': 'change',
                'value': data1[key],
                'new_value': data2[key]
            })

    return differ


def generate_diff(first_file_path, second_file_path):
    data1 = get_data(first_file_path)
    data2 = get_data(second_file_path)
    diff = get_diff(data1, data2)
    return diff
