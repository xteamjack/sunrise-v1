"""Download the Bitext customer-support dataset and save the raw train split.

Source: https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset
"""

from pathlib import Path

from datasets import load_dataset

DATASET = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"
OUT_DIR = Path("data/opensource")
OUT_PATH = OUT_DIR / "bitext_raw.parquet"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    ds = load_dataset(DATASET, split="train")
    df = ds.to_pandas()
    df.to_parquet(OUT_PATH, index=False)

    print(f"Saved {len(df):,} rows to {OUT_PATH}")
    print(f"Columns: {list(df.columns)}")
    print("\nTop intents:")
    print(df["intent"].value_counts().head(15).to_string())


if __name__ == "__main__":
    main()
