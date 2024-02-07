from gendiff.formatting import stylish, plain


def formating(diff, format_):
    if format_ == 'stylish':
        return stylish.stylish(diff)
    elif format_ == 'plain':
        return plain.plain(diff)
