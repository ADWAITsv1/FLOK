# logic/apriori_matcher.py

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def learn_rules_from_history(csv_path, min_support=0.3, min_conf=0.7):
    df = pd.read_csv(csv_path)

    # Combine items into transactions
    transactions = []
    for _, row in df.iterrows():
        transaction = [
            row["FoodType"],
            row["Location"],
            f"Expiry<{int(row['ExpiryHrs'])}",
            row["MatchedReceiver"]
        ]
        transactions.append(transaction)

    te = TransactionEncoder()
    te_data = te.fit(transactions).transform(transactions)
    df_trans = pd.DataFrame(te_data, columns=te.columns_)

    freq_items = apriori(df_trans, min_support=min_support, use_colnames=True)
    rules = association_rules(freq_items, metric="confidence", min_threshold=min_conf)

    return rules

def get_apriori_recommendation(food_type, location, expiry_hrs, rules_df):
    expiry_tag = f"Expiry<{int(expiry_hrs)}"

    for _, row in rules_df.iterrows():
        if {food_type, location, expiry_tag}.issubset(row["antecedents"]):
            consequents = list(row["consequents"])
            return consequents[0] if consequents else "No prediction"

    return "No prediction"
