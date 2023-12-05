import pytest
from string_utils import StringUtils

strings = StringUtils()

@pytest.mark.parametrize('list_, joiner_, res_', [
    ([1,2,3,4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([],"","")
    ])
def test_list_to_string(list_, joiner_, res_):
    res = strings.list_to_string(list_,  joiner_)
    assert res == res_

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('list_, joiner_, res_', [
    ([1,2,3,4], ", ", "1,2,3,4"),
    (["Sky", "Pro"], ", ", "Sky Pro"),
    (["Sky", "Pro"], "-", "Sky--Pro"),
    ([],""," ")
    ])
def test_list_to_string_negative(list_, joiner_, res_):
    res = strings.list_to_string(list_,  joiner_)
    assert res == res_

@pytest.mark.parametrize('string_, delimeter_, res_', [
    ("a, b, c, d", ", ", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("",",",[]),
    (" , ",",",[" "," "])
    ])
def test_to_list(string_, delimeter_, res_):
    res = strings.to_list(string_, delimeter_)
    assert res == res_

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string_, delimeter_, res_', [
    ("a,b,c,d", ", ", ["a", "b", "c", "d"]),
    ("1:2:3", ".", ["1", "2", "3"]),
    (" , ",",",[" "])
    ])
def test_to_list_negative(string_, delimeter_, res_):
    res = strings.to_list(string_, delimeter_)
    assert res == res_


def test_contains():
    assert strings.contains("AssertionError", 'r')

@pytest.mark.xfail(strict=True)
def test_contains_negative():
    assert strings.contains("AssertionError", 'R')


def test_end_with():
    assert strings.end_with("Word", 'd')

@pytest.mark.xfail(strict=True)
def test_end_with_negative():
        assert strings.end_with("Word", 'D')


def test_starts_with():
    assert strings.starts_with("Words", 'W')

@pytest.mark.xfail(strict=True)
def test_starts_with_negative():
    assert strings.starts_with("Words", 'w')


def test_capitilize():
    res = strings.capitilize("communication")
    assert res == "Communication"

@pytest.mark.xfail(strict=True)
def test_capitilize_negative():
    res = strings.capitilize("communication")
    assert res == "communication"

@pytest.mark.parametrize('string_, symbol_, res_', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Sky Pro", "y P", "Skro"),
    (" "," ","")
    ])
def test_delete_symbol(string_, symbol_, res_):
    res = strings.delete_symbol(string_, symbol_)
    assert res == res_

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string_, symbol_, res_', [
    ("SkyPro", "k", "SkyPro"),
    ("SkyPro", "Pro", "SkySky"),
    ("Sky Pro", "y P", "Sk ro")
    ])
def test_delete_symbol_negative(string_, symbol_, res_):
    res = strings.delete_symbol(string_, symbol_)
    assert res == res_

@pytest.mark.parametrize('string_',[
    (""),
    (" "),
    ("  "),
    ("       ")
    ])
def test_is_empty(string_):
    assert strings.is_empty(string_)

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('string_',[
    ("a"),
    (" b")
    ])
def test_is_empty_negative(string_):
    assert strings.is_empty(string_)

@pytest.mark.parametrize('string_, res_', [
    ("word", "word"),
    (" word", "word"),
    ("     word", "word"),
    (" ", ""),
    ("","")
    ])
def test_trim(string_, res_):
    res = strings.trim(string_)
    assert res == res_

