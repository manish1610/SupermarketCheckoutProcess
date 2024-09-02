from typing import Dict
from cart import Cart
from store import Discount


class PricingRule:
    def __init__(self, discounts: Dict[str, Discount]):
        self.discounts: Dict[str, Discount] = discounts

    def calculate_total(self, cart: Cart) -> int:
        total: int = 0
        for item, quantity in cart.get_items().items():
            discount = self.discounts.get(item.name)

            if discount:
                num_discounts = quantity // discount.quantity
                remainder = quantity % discount.quantity
                total += num_discounts * discount.discount_price + remainder * item.price
            else:
                total += quantity * item.price

        return total
