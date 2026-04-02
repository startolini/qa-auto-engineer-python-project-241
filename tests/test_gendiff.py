import os

import pytest

from gendiff import generate_diff

TEST_DATA = os.path.join(os.path.dirname(__file__), 'test_data')


def get_path(filename):
    return os.path.join(TEST_DATA, filename)


@pytest.fixture
def expected():
    with open(os.path.join(TEST_DATA, 'expected_diff.txt')) as f:
        return f.read()


@pytest.fixture
def expected_plain():
    with open(os.path.join(TEST_DATA, 'expected_plain.txt')) as f:
        return f.read()


@pytest.fixture
def expected_json():
    with open(os.path.join(TEST_DATA, 'expected_json.txt')) as f:
        return f.read()


def test_generate_diff_json_fmt(expected):
    result = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert result == expected


def test_generate_diff_yaml(expected):
    result = generate_diff(get_path('file1.yml'), get_path('file2.yml'))
    assert result == expected


def test_generate_diff_plain(expected_plain):
    result = generate_diff(
        get_path('file1.json'), get_path('file2.json'), 'plain'
    )
    assert result == expected_plain


def test_generate_diff_json(expected_json):
    result = generate_diff(
        get_path('file1.json'), get_path('file2.json'), 'json'
    )
    assert result == expected_json
