import pytest
from classes import Product

@pytest.fixture
def new_item():
    return Product('test_name', 1000, 10)

def test_get_total_amount(new_item):
    assert new_item.get_total_amount() == 10000

def test_set_discount(new_item):
    assert new_item.set_discount() == 850

def test_repr(new_item):
    assert new_item.__repr__() == 'Product - test_name, price - 1000, amount - 10'
