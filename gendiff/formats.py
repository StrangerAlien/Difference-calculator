from gendiff.formatting import stylish, plain, make_json


def formating(diff, format_):
    if format_ == 'stylish':
        return stylish.stylish(diff)
    elif format_ == 'plain':
        return plain.plain(diff)
    elif format_ == 'json':
        return make_json.make_json(diff)
