"""Shared configuration for the synthetic data generators.

Everything the generators need to be deterministic and consistent lives here:
one fixed SEED, the output folders, the dataset sizes, the business-case intent
mix, and the product category list.
"""

from pathlib import Path

# One seed for every generator, so a rebuild is reproducible.
SEED = 20260101

# Output folders (relative to the base, sunrise-v1).
GENERATED_DIR = Path("data/generated")
KNOWLEDGE_DIR = Path("data/knowledge")
EVAL_DIR = Path("data/eval")
OPENSOURCE_DIR = Path("data/opensource")

# Dataset sizes.
N_PRODUCTS = 300
N_ORDERS = 5000
N_TICKETS = 3000

# Business-case intent mix (must sum to 1.0).
INTENT_MIX = {
    "order_status": 0.30,
    "returns": 0.18,
    "warranty": 0.12,
    "other": 0.40,
}

# Product categories for Sunrise Electronics.
CATEGORIES = [
    "Mobiles",
    "Laptops",
    "Televisions",
    "Headphones",
    "Cameras",
    "Refrigerators",
    "WashingMachines",
    "AirConditioners",
    "Speakers",
    "Accessories",
]

# Rupee price band and warranty (months) per category.
CATEGORY_SPECS = {
    "Mobiles": {"prefix": "MOB", "price": (8000, 150000), "warranty": (12, 24)},
    "Laptops": {"prefix": "LAP", "price": (30000, 250000), "warranty": (12, 36)},
    "Televisions": {"prefix": "TEL", "price": (15000, 300000), "warranty": (12, 36)},
    "Headphones": {"prefix": "HPH", "price": (500, 40000), "warranty": (6, 24)},
    "Cameras": {"prefix": "CAM", "price": (5000, 200000), "warranty": (12, 24)},
    "Refrigerators": {"prefix": "REF", "price": (12000, 90000), "warranty": (24, 120)},
    "WashingMachines": {"prefix": "WAS", "price": (10000, 70000), "warranty": (24, 60)},
    "AirConditioners": {"prefix": "AIR", "price": (25000, 80000), "warranty": (12, 60)},
    "Speakers": {"prefix": "SPK", "price": (800, 50000), "warranty": (6, 24)},
    "Accessories": {"prefix": "ACC", "price": (200, 8000), "warranty": (6, 12)},
}

# The one threshold the canon fixes for money.
REFUND_APPROVAL_INR = 5000
