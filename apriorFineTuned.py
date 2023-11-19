import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Load the dataset
csv_path = 'Market_Basket_Optimisation.csv'
items_data_df = pd.read_csv(csv_path, header=None)
print(items_data_df.head())

# Check unique items
unique_items = items_data_df[0].unique()
print(unique_items)

# Perform one-hot encoding
encoded_vals = []
for i, rows in items_data_df.iterrows():
    labels = {}
    uncommons = list(set(unique_items) - set(rows))
    commons = list(set(unique_items).intersection(rows))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)

encode_df = pd.DataFrame(encoded_vals)
print(encode_df.head())

# Apply Apriori algorithm
encode_df = encode_df.astype(bool)  # Convert DataFrame to boolean type
freq_items = apriori(encode_df, min_support=0.0085, use_colnames=True, verbose=1, low_memory=False)
print(freq_items.head())

# Find association rules based on confidence
assocn_rules_conf = association_rules(freq_items, metric="confidence", min_threshold=0.25)
print(assocn_rules_conf)

# Find association rules based on support
assocn_rules_supp = association_rules(freq_items, metric="support", min_threshold=0.50)
print(assocn_rules_supp)

# Plotting the scatter plot of Confidence Vs Support
plt.scatter(assocn_rules_conf['support'], assocn_rules_conf['confidence'], alpha=.11)
plt.xlabel('support')
plt.ylabel('confidence')
plt.title('Support vs Confidence')
plt.savefig('Support_vs_Confidence.png')
plt.show()

# Plotting the scatter plot of Lift Vs Support
plt.scatter(assocn_rules_conf['support'], assocn_rules_conf['lift'], alpha=0.5)
plt.xlabel('support')
plt.ylabel('lift')
plt.title('Support vs Lift')
plt.savefig('Support_vs_Lift.png')
plt.show()


# Writing the generated rules based on confidence to an Excel file for business use
assocn_rules_conf.to_excel('Generated_Rules_conf.xlsx', 'Rules', index=False)


# Writing the generated rules based on support to an Excel file for business use
assocn_rules_supp.to_excel('Generated_Rules_supp.xlsx', 'Rules', index=False)


# Code to find the best confidence rules
best_conf_rules = assocn_rules_conf.sort_values(by='confidence', ascending=False).head(10)

# Code to find the best support rules
best_supp_rules = assocn_rules_supp.sort_values(by='support', ascending=False).head(10)

# Writing the best confidence rules to an Excel file
best_conf_rules.to_excel('Best_Confidence_Rules.xlsx', 'Best Confidence Rules', index=False)


# Writing the best support rules to an Excel file
best_supp_rules.to_excel('Best_Support_Rules.xlsx', 'Best Support Rules', index=False)


# Generating recommendations based on the best confidence rules
recommendations_conf = []
for index, row in best_conf_rules.iterrows():
    antecedents = ', '.join(list(row['antecedents']))
    consequents = ', '.join(list(row['consequents']))
    recommendations_conf.append(f"If you buy {antecedents}, you may also like {consequents}.")

# Generating recommendations based on the best support rules
recommendations_supp = []
for index, row in best_supp_rules.iterrows():
    antecedents = ', '.join(list(row['antecedents']))
    consequents = ', '.join(list(row['consequents']))
    recommendations_supp.append(f"If you buy {antecedents}, you may also like {consequents}.")

# Check the lengths of both recommendation lists
print(len(recommendations_conf), len(recommendations_supp))

# Ensure both recommendation lists have the same length
min_length = min(len(recommendations_conf), len(recommendations_supp))
recommendations_conf = recommendations_conf[:min_length]
recommendations_supp = recommendations_supp[:min_length]

# Writing recommendations to an Excel file
recommendations_df = pd.DataFrame({
    'Best Confidence Rules Recommendations': recommendations_conf,
    'Best Support Rules Recommendations': recommendations_supp
})
recommendations_df.to_excel('Recommendations.xlsx', 'Recommendations', index=False)
