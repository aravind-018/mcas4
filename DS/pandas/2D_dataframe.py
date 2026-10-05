import pandas as pd

listdata = [
    [1, "Alice", 10],
    [2, "Bob", 15],
    [3, "Don", 25]
]

df = pd.DataFrame(
    listdata,
    columns=["ID", "Name", "Score"]
)

print(df)