from gendiff.make_str import make_str

INDENT = ' '
SPACES_COUNT = 4


def stylish(diff, depth=0):
    result = ['{']
    offset = depth + SPACES_COUNT
    for node in diff:

        key, type = node.get('key'), node.get('type')
        value, new_value = node.get('value'), node.get('new_value')
        value_str = deep_line(value)
        new_value_str = deep_line(new_value)

        spaces = INDENT * (offset - 2)

        added = f'{spaces}+ {key}: {value_str}'
        removed = f'{spaces}- {key}: {value_str}'
        samed = f'{spaces}  {key}: {value_str}'
        changed = f'{spaces}+ {key}: {new_value_str}'

        if type == 'add':
            result.append(added)
        elif type == 'remove':
            result.append(removed)
        elif type == 'same':
            result.append(samed)
        elif type == 'change':
            result.append(removed)
            result.append(changed)
        elif type == 'children':
            result.append(f'{INDENT * offset}{key}: '
                          + stylish(value, offset))

    result.append(f'{INDENT * depth + "}"}')
    return '\n'.join(result)


def deep_line(value, depth=0):
    if not isinstance(value, dict):
        return make_str(value)
    lines = ['{']
    for key in value.keys():
        current = value[key]
        format_key = f'{INDENT * (depth + SPACES_COUNT * 2)}{key}: '
        if isinstance(current, dict):
            lines.append(format_key
                         + deep_line(current, depth + SPACES_COUNT))
        else:
            lines.append(format_key + make_str(current))
    lines.append(f'{INDENT * (depth + SPACES_COUNT) + "}"}')
    return '\n'.join(lines)
