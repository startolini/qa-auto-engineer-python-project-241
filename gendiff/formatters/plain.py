def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return value


def render(diff):
    lines = []
    for key, status, val1, val2 in diff:
        if status == 'removed':
            lines.append(f"Property '{key}' was removed")
        elif status == 'added':
            lines.append(
                f"Property '{key}' was added with value: {format_value(val2)}"
            )
        elif status == 'changed':
            lines.append(
                f"Property '{key}' was updated."
                f" From {format_value(val1)} to {format_value(val2)}"
            )
    return '\n'.join(lines)
