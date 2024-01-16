from gendiff.parse_file import get_data


def generate_diff(first_file_path, second_file_path):
    file1 = get_data(first_file_path)
    file2 = get_data(second_file_path)

    nodes = ['{']
    keys = sorted(set(file1.keys()) | set(file2.keys()))

    for key in keys:
        if key not in file1:
            nodes.append(f'  + {key}: {file2[key]}')
        elif key not in file2:
            nodes.append(f'  - {key}: {file1[key]}')
        elif file1[key] == file2[key]:
            nodes.append(f'    {key}: {file2[key]}')
        else:
            nodes.append(f'  - {key}: {file1[key]}')
            nodes.append(f'  + {key}: {file2[key]}')
    return '\n'.join(nodes) + '\n}\n'
