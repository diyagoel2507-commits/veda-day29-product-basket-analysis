import pandas as pd
from itertools import combinations

DATA_PATH = "data/retail_transactions.csv"

df = pd.read_csv(DATA_PATH)

# One basket = all products purchased under the same OrderID
baskets = df.groupby("OrderID")["Product"].apply(set)

pair_counts = {}
for items in baskets:
    for pair in combinations(sorted(items), 2):
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

pairs = pd.DataFrame(
    [(a, b, count) for (a, b), count in pair_counts.items()],
    columns=["Product_A", "Product_B", "Orders_Together"]
)

pairs["Support_%"] = (pairs["Orders_Together"] / len(baskets) * 100).round(2)
pairs = pairs.sort_values("Orders_Together", ascending=False)

pairs.to_csv("outputs/product_pairs.csv", index=False)
pairs.head(10).to_csv("outputs/top_product_pairs.csv", index=False)

# Product recommendations
recommendations = []
for product in sorted(df["Product"].unique()):
    matches = pairs[
        (pairs["Product_A"] == product) |
        (pairs["Product_B"] == product)
    ].copy()

    matches["Recommended_Product"] = matches.apply(
        lambda row: row["Product_B"]
        if row["Product_A"] == product else row["Product_A"],
        axis=1
    )

    for _, row in matches.head(3).iterrows():
        recommendations.append({
            "Product": product,
            "Recommended_Product": row["Recommended_Product"],
            "Orders_Together": int(row["Orders_Together"]),
            "Support_%": row["Support_%"]
        })

pd.DataFrame(recommendations).to_csv(
    "outputs/recommendations.csv", index=False
)

print("Analysis complete.")
print("\nTop 10 product pairs:")
print(pairs.head(10).to_string(index=False))
