import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    """Creates prices in stripe."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Donation"},
    )


def create_stripe_session(price):
    """Creates payment session in stripe."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
