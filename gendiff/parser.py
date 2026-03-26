import json
import os

import yaml


def parse(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path) as f:
        if ext == '.json':
            return json.load(f)
        if ext in ('.yml', '.yaml'):
            return yaml.safe_load(f)
    raise ValueError(f'Unsupported format: {ext}')
