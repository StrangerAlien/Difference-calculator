from gendiff import read_file

file1 = read_file.file1
file2 = read_file.file2


def generate_diff(data1, data2):
    nodes = ['{']
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in keys:
        if key not in data1:
            nodes.append(f'  + {key}: {data2[key]}')
        elif key not in data2:
            nodes.append(f'  - {key}: {data1[key]}')
        elif data1[key] == data2[key]:
            nodes.append(f'    {key}: {data2[key]}')
        else:
            nodes.append(f'  - {key}: {data1[key]}')
            nodes.append(f'  + {key}: {data2[key]}')
    return '\n'.join(nodes) + '\n}'


print(generate_diff(file1, file2))
