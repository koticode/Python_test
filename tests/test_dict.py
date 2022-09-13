import pytest

from main import numeration

def test_key_exist_dict():
    assert 1 in numeration.keys()

def test_key_exist_dict2():
    assert len(numeration) == 3

# параметризованный тест. Т.к. формат словаря такой, что каждой цифре должно соответствовать слово, передаю 3 кортежа с парами значений (избыточных значений нет)

@pytest.mark.parametrize("key,value", [(1, 'one'),(2, "two"), (3, 'three')])
def test_pairs(key, value):
    assert numeration.get(key)==value

