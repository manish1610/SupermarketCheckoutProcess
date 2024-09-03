from pricing import PricingRule
from store import Item, Store, Discount
from typing import Dict


def setup_store() -> Store:
    store = Store()
    store.add_item(Item('A', 50))
    store.add_item(Item('B', 30))
    store.add_item(Item('C', 20))
    store.add_item(Item('D', 15))

    return store


def setup_discounts(store: Store) -> Dict[str, Discount]:
    item_a = store.get_item("A")
    item_b = store.get_item("B")

    return {
        'A': Discount(item_a, 3, 130),
        'B': Discount(item_b, 2, 45),
    }


def setup():
    store = setup_store()
    discounts = setup_discounts(store)
    pricing_rule = PricingRule(discounts)

    return store, discounts, pricing_rule
