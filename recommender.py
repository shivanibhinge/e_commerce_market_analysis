# recommender.py

import pandas as pd
from collections import Counter

# -------------------------
# Load data once on start
# -------------------------
df = pd.read_csv("retail_combined.csv")
df.rename(columns={'Invoice':'InvoiceNo', 'Customer ID':'CustomerID', 'Price':'UnitPrice'}, inplace=True)
df = df.dropna()
df.InvoiceDate = pd.to_datetime(df.InvoiceDate)

# clean data
df = df[(df['UnitPrice'] > 0) & (df['Quantity'] > 0)]
df['StockCode'] = df['StockCode'].astype(str).str[:-1]

# product reference
product_df = df.groupby(['StockCode', 'Description']).Quantity.sum().reset_index()
product_df.StockCode = product_df.StockCode.apply(lambda x: x if x.isdigit() else None)
product_df = product_df.dropna()

product_lookup = {row["StockCode"]: row["Description"] for _, row in product_df.iterrows()}

# keyword dictionary
word_index = {code: desc.lower().split() for code, desc in product_lookup.items()}

# transaction baskets
baskets = df.groupby("InvoiceNo")["StockCode"].apply(list).tolist()
baskets = [b for b in baskets if len(b) <= 50]


def get_stockcode(words):
    for sc, wordlist in word_index.items():
        if set(words).issubset(set(wordlist)):
            return sc
    return None


# -------------------------
# Main recommend function
# -------------------------
def recommend(query):
    words = query.lower().split()
    sc = get_stockcode(words)

    if not sc:
        return f"No matching product found for: '{query}'"

    co_items = []
    for basket in baskets:
        if sc in basket:
            co_items.extend([item for item in basket if item != sc])

    if not co_items:
        return f"No recommendations available for: '{query}'"

    ranked = Counter(co_items).most_common()

    result_lines = []
    seen = set()

    for product, count in ranked:
        if product in product_lookup and product_lookup[product] not in seen:
            result_lines.append(f"{len(result_lines)+1}. {product_lookup[product]} ({count} purchases)")
            seen.add(product_lookup[product])

        if len(result_lines) == 10:
            break

    output = f'Because users bought "{query}", they also frequently purchased:\n' + "\n".join(result_lines)
    return output
