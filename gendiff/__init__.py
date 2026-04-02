from gendiff.formatters import plain, stylish
from gendiff.parser import parse


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = []
    for key in keys:
        if key not in data2:
            diff.append((key, 'removed', data1[key], None))
        elif key not in data1:
            diff.append((key, 'added', None, data2[key]))
        elif data1[key] == data2[key]:
            diff.append((key, 'unchanged', data1[key], None))
        else:
            diff.append((key, 'changed', data1[key], data2[key]))
    return diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = build_diff(data1, data2)
    if formatter == 'stylish':
        return stylish.render(diff)
    if formatter == 'plain':
        return plain.render(diff)
    raise ValueError(f'Unknown formatter: {formatter}')
