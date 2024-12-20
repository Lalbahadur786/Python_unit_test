from shopping_cart import ShoppingCart
from unittest.mock import Mock
from items_database import ItemDatabase
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add('milk')
    assert cart.size() == 1

def test_can_get_item_when_added_to_cart(cart):
    cart.add('milk')
    assert 'milk' in cart.get_items()

def test_when_add_more_than_max_items_should_fail(cart):
    for item in ['milk', 'bread', 'eggs', 'cheese', 'butter']:
        cart.add(item)
    with pytest.raises(OverflowError):
        cart.add('Ghee')
    
def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('banana')
    item_database = ItemDatabase()
    def mock_get_item(item: str):
        if item == 'apple':
            return 1.0
        if item == 'banana':
            return 2.0
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0