def get_diff(data1, data2):

    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in keys:
        if key not in data1.keys():
            diff.append({
                'key': key,
                'type': 'add',
                'value': data2[key]
            })
        elif key not in data2.keys():
            diff.append({
                'key': key,
                'type': 'remove',
                'value': data1[key]
            })
        elif isinstance(data1.get(key), dict) and \
                isinstance(data2.get(key), dict):
            diff.append({
                'key': key,
                'type': 'children',
                'value': get_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'type': 'same',
                'value': data1[key]
            })
        else:
            diff.append({
                'key': key,
                'type': 'change',
                'value': data1[key],
                'new_value': data2[key]
            })
    return diff
