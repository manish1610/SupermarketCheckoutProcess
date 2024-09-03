from checkout import Checkout
from cart import Cart
from setup import setup


class Run:
    def __init__(self):
        self.store, self.discounts, self.pricing_rule = setup()

    def process_input(self, input_str):
        cart = Cart()
        for item_name in input_str:
            item = self.store.get_item(item_name)
            cart.add_item(item)

        checkout = Checkout(cart, self.pricing_rule)

        return checkout.total()


if __name__ == "__main__":
    run = Run()
    inputs = [
        "",
        "A",
        "AB",
        "CDBA",
        "AA",
        "AAA",
        "AAAA",
        "AAAAA",
        "AAAAAA",
        "AAAB",
        "AAABB",
        "AAABBD",
        "DABABA"
    ]

    for input_str in inputs:
        print(f"Input: {input_str} -> Total: {run.process_input(input_str)}")
