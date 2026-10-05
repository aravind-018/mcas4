import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "profit": [1000, -500, 0]
}

df = pd.DataFrame(data)

df["profit"] = df["profit"] > 0

print("Profit Column Converted to Boolean:\n", df)