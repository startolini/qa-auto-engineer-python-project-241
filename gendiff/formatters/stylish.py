def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def render(diff):
    lines = []
    for key, status, val1, val2 in diff:
        if status == 'removed':
            lines.append(f'  - {key}: {format_value(val1)}')
        elif status == 'added':
            lines.append(f'  + {key}: {format_value(val2)}')
        elif status == 'unchanged':
            lines.append(f'    {key}: {format_value(val1)}')
        elif status == 'changed':
            lines.append(f'  - {key}: {format_value(val1)}')
            lines.append(f'  + {key}: {format_value(val2)}')
    return '{{\n{}\n}}'.format('\n'.join(lines))
