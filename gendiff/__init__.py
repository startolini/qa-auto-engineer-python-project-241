from gendiff.parser import parse


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    keys = sorted(data1.keys() | data2.keys())
    lines = []

    for key in keys:
        if key not in data2:
            lines.append(f'  - {key}: {format_value(data1[key])}')
        elif key not in data1:
            lines.append(f'  + {key}: {format_value(data2[key])}')
        elif data1[key] == data2[key]:
            lines.append(f'    {key}: {format_value(data1[key])}')
        else:
            lines.append(f'  - {key}: {format_value(data1[key])}')
            lines.append(f'  + {key}: {format_value(data2[key])}')

    return '{{\n{}\n}}'.format('\n'.join(lines))


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
