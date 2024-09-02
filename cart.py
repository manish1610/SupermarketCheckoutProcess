from typing import Dict
from store import Item


class Cart:
    def __init__(self):
        self.items: Dict[Item, int] = {}

    def add_item(self, item: Item) -> None:
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def get_items(self) -> Dict[Item, int]:
        return self.items
