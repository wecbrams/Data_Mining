import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load the data from CSV
file_path = 'Market_Basket_Optimisation.csv'  # Replace 'your_data.csv' with your actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
print("Data preview:")
print(data.head())

# Convert the data to a list of lists (transactions)
transactions = []
for row in data.values:
    transactions.append([str(item) for item in row if pd.notna(item)])

# Use TransactionEncoder to one-hot-encode the transactions
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
min_support = 0.2  # Adjust the support threshold as needed
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

# Display frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display association rules
print("\nAssociation Rules:")
print(rules)
