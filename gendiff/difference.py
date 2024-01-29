from gendiff.parse_file import get_data


def generate_diff(first_file_path, second_file_path):
    file1 = get_data(first_file_path)
    file2 = get_data(second_file_path)

    diff = []
    keys = sorted(set(file1.keys()) | set(file2.keys()))

    for key in keys:
        if key not in file1.keys():
            diff.append({
                'key': key,
                'type': 'add',
                'value': file2[key]
            })
        elif key not in file2.keys():
            diff.append({
                'key': key,
                'type': 'remove',
                'value': file1[key]
            })
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff.append({
                'key': key,
                'type': 'children',
                'value': generate_diff(file1[key], file2[key])
            })
        elif file1[key] == file2[key]:
            diff.append({
                'key': key,
                'type': 'same',
                'value': file1[key]
            })
        else:
            diff.append({
                'key': key,
                'type': 'change',
                'value': file1[key],
                'new_value': file2[key]
            })

    return diff
