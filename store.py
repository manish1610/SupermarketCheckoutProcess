from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int

    def __hash__(self) -> int:
        return hash((self.name, self.price))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Item):
            return (self.name, self.price) == (other.name, other.price)
        return False


@dataclass
class Discount:
    item: Item
    quantity: int
    discount_price: int


class Store:
    def __init__(self):
        self.items: dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        self.items[item.name] = item

    def get_item(self, item_name: str) -> Item | None:
        return self.items.get(item_name)
