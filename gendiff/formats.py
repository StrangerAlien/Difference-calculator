from gendiff.formatting import stylish, plain, make_json


def formating(diff, format_name):
    if format_name == 'stylish':
        return stylish.stylish(diff)
    elif format_name == 'plain':
        return plain.plain(diff)
    elif format_name == 'json':
        return make_json.make_json(diff)
    else:
        raise ValueError('Unknown format')
