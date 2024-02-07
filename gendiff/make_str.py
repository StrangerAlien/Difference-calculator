def make_str(string_value):
    return str(string_value).lower() if isinstance(string_value, bool) \
        else "null" if string_value is None else str(string_value)
