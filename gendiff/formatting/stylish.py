INDENT = ' '
SPACES_COUNT = 4


def stylish(diff):
    def iter(tree, depth=0):

        result = ['{']
        offset = depth + SPACES_COUNT
        for node in tree:

            key, type = node.get('key'), node.get('type')
            value, new_value = node.get('value'), node.get('new_value')
            value_str = stringify(value)
            new_value_str = stringify(new_value)
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
                              + iter(value, offset))

        result.append(f'{INDENT * depth + "}"}')
        return '\n'.join(result)

    return iter(diff)


def make_str(string_value):
    return str(string_value).lower() if isinstance(string_value, bool) \
        else "null" if string_value is None else str(string_value)


def stringify(value, depth=0):
    if not isinstance(value, dict):
        return make_str(value)
    lines = ['{']
    for key in value.keys():
        current = value[key]
        format_key = f'{INDENT * (depth + SPACES_COUNT * 2)}{key}: '
        if isinstance(current, dict):
            lines.append(format_key
                         + stringify(current, depth + SPACES_COUNT))
        else:
            lines.append(format_key + make_str(current))
    lines.append(f'{INDENT * (depth + SPACES_COUNT) + "}"}')
    return '\n'.join(lines)
