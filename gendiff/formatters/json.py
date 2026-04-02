import json


def render(diff):
    result = []
    for key, status, val1, val2 in diff:
        node = {'key': key, 'status': status}
        if status in ('removed', 'unchanged'):
            node['value'] = val1
        elif status == 'added':
            node['value'] = val2
        elif status == 'changed':
            node['old'] = val1
            node['new'] = val2
        result.append(node)
    return json.dumps(result, indent=2)
