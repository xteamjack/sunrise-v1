"""Generate the product catalog: 300 products across the categories.

Deterministic from config.SEED. Prices are rupees (int). Uses Faker en_IN.
Saves data/generated/catalog.json.
"""

import json
import random

from faker import Faker

from data.config import CATEGORIES, CATEGORY_SPECS, GENERATED_DIR, N_PRODUCTS, SEED
from domain.models import Product

OUT_PATH = GENERATED_DIR / "catalog.json"


def main() -> None:
    random.seed(SEED)
    fake = Faker("en_IN")
    Faker.seed(SEED)

    per_category = N_PRODUCTS // len(CATEGORIES)
    products: list[Product] = []

    for category in CATEGORIES:
        spec = CATEGORY_SPECS[category]
        lo, hi = spec["price"]
        wlo, whi = spec["warranty"]
        for n in range(1, per_category + 1):
            sku = f"{spec['prefix']}-{n:03d}"
            name = f"{fake.company()} {category[:-1] if category.endswith('s') else category} {fake.bothify('??-###').upper()}"
            price_inr = random.randint(lo // 100, hi // 100) * 100
            warranty_months = random.choice(range(wlo, whi + 1, 6)) if whi > wlo else wlo
            products.append(
                Product(
                    sku=sku,
                    name=name,
                    category=category,
                    price_inr=price_inr,
                    warranty_months=warranty_months,
                )
            )

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        json.dumps([p.model_dump() for p in products], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    prices = [p.price_inr for p in products]
    print(f"catalog: {len(products)} products across {len(CATEGORIES)} categories -> {OUT_PATH}")
    print(f"  per category: {per_category}")
    print(f"  price range: Rs {min(prices):,} to Rs {max(prices):,}")


if __name__ == "__main__":
    main()
