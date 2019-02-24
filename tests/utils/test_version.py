from mpl.utils.version import get_version
import pytest


TEST_VERSION = ["0", "0", "1"]


def test_should_return_a_string():
    assert isinstance(get_version([]), str)


def test_should_return_raise_type_exception():
    with pytest.raises(TypeError):
        get_version(map(int, TEST_VERSION))


def test_should_return_a_empity_string():
    assert get_version([]) == ""


def test_should_return_exactly_version():
    assert get_version(TEST_VERSION) == "001"
