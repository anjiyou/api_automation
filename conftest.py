"""
@Filename:/conftest
@Author:刘威
@Time:2022/7/30 16:57
@Describe:...
"""
import pytest

from commons.yaml_util import clean_yaml

@pytest.fixture(scope="session",autouse=True)
def clean_extract_yaml():
    clean_yaml("extract.yaml")