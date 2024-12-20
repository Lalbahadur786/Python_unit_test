from typing import List

class ShoppingCart:
    def __init__(self, max_items: int):
        self.items: List[str] = []
        self.max_items = max_items

    def add(self, item: str):
        if self.size() >= self.max_items:
            raise OverflowError('Cart is full')
        self.items.append(item)

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price(self, price_map):
        total = 0.0
        for item in self.items:
            total += price_map.get(item)
        return total
    