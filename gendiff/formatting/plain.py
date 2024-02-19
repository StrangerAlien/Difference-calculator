def plain(diff, path=''):
    result = []
    for node in diff:

        key, type = node.get('key'), node.get('type')
        value, new_value = node.get('value'), node.get('new_value')
        value_str = deep_line(value)
        new_value_str = deep_line(new_value)

        new_path = key if path == '' else f'{path}.{key}'
        added = f"Property '{new_path}' was added with value: {value_str}"
        removed = f"Property '{new_path}' was removed"
        changed = f"Property '{new_path}' was updated. " \
                  + f"From {value_str} to {new_value_str}"

        if type == 'add':
            result.append(added)
        elif type == 'remove':
            result.append(removed)
        elif type == 'change':
            result.append(changed)
        elif type == 'children':
            result.append(plain(value, new_path))
    return '\n'.join(result)


def deep_line(value):
    if isinstance(value, dict):
        return '[complex value]'
    new_value = f"'{value}'" if isinstance(value, str) else value

    return str(new_value).lower() if isinstance(new_value, bool) \
        else "null" if new_value is None else str(new_value)
