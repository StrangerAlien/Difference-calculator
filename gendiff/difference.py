from gendiff import read_file

file1 = read_file.file1
file2 = read_file.file2


def generate_diff(file1, file2):
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
    return '\n'.join(nodes) + '\n}'


print(generate_diff(file1, file2))
