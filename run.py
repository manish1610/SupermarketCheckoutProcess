from checkout import Checkout
from cart import Cart
from pricing import PricingRule
from setup import setup_store, setup_discounts


def process_input(input_str: str) -> int:
    store = setup_store()
    discounts = setup_discounts(store)
    pricing_rule = PricingRule(discounts)

    cart = Cart()
    for item_name in input_str:
        item = store.get_item(item_name)
        cart.add_item(item)

    checkout = Checkout(cart, pricing_rule)

    return checkout.total()


if __name__ == "__main__":
    test_inputs = [
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

    for input_str in test_inputs:
        print(f"Input: {input_str} -> Total: {process_input(input_str)}")
