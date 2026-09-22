"""Transform the raw Bitext data into an order/refund ticket seed.

Keeps only order and refund intents, maps them to our ticket types
(order_status, returns, other), and scrubs email / phone patterns from the
customer text. Saves data/opensource/tickets_seed.parquet.
"""

import re
from pathlib import Path

import pandas as pd

IN_PATH = Path("data/opensource/bitext_raw.parquet")
OUT_PATH = Path("data/opensource/tickets_seed.parquet")

# Bitext intents -> our ticket types.
ORDER_INTENTS = {"cancel_order", "change_order", "place_order", "track_order"}
REFUND_INTENTS = {"check_refund_policy", "get_refund", "track_refund"}


def to_type(intent: str) -> str:
    if intent in ORDER_INTENTS:
        return "order_status"
    if intent in REFUND_INTENTS:
        return "returns"
    return "other"


EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
# 7+ digits with common separators, optional country code.
PHONE_RE = re.compile(r"(?<!\w)\+?\d[\d\s().-]{6,}\d(?!\w)")


def scrub(text: str) -> str:
    text = EMAIL_RE.sub("{{EMAIL}}", text)
    text = PHONE_RE.sub("{{PHONE}}", text)
    return text


def main() -> None:
    df = pd.read_parquet(IN_PATH)

    keep = ORDER_INTENTS | REFUND_INTENTS
    df = df[df["intent"].isin(keep)].copy()

    df["ticket_type"] = df["intent"].map(to_type)
    df["text"] = df["instruction"].astype(str).map(scrub)

    out = df[["text", "intent", "category", "ticket_type"]].reset_index(drop=True)
    out.to_parquet(OUT_PATH, index=False)

    print(f"Saved {len(out):,} rows to {OUT_PATH}")
    print("\nTicket type counts:")
    print(out["ticket_type"].value_counts().to_string())
    print("\nIntent counts:")
    print(out["intent"].value_counts().to_string())


if __name__ == "__main__":
    main()
