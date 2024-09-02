from cart import Cart
from pricing import PricingRule


class Checkout:
    def __init__(self, cart: Cart, pricing_rule: PricingRule):
        self.cart: Cart = cart
        self.pricing_rule: PricingRule = pricing_rule

    def total(self) -> int:
        return self.pricing_rule.calculate_total(self.cart)
