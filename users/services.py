import stripe
from forex_python.converter import CurrencyRates

stripe.api_key = "sk_test_51PwQ0DGtRQgxkxdjaPE1m9OP8k7C4ZFH5TuxxNFLYlXj42vlaQO3NxdxFWgs45EnukxLqGerHJNYBMp01NqiM4st006zReoYs3"


def create_stripe_product(prod):
    """Создает продукт в страйпе"""
    title_product = f"{prod.course}" if prod.course else prod.lesson
    product = stripe.Product.create(name=title_product)
    return product.get('id')


def convert_rub_to_usd(amount):
    """Конвертирует рубли в доллары"""
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(rate * amount)


def create_stripe_price(amount, product_id):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )


def create_stripe_sessions(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')