# flok_blockchain.py

import pandas as pd
import json
from datetime import datetime
from logic.semantic_rules import evaluate_risk, is_urgent
from logic.receiver_registry import match_receiver
from logic.apriori_matcher import learn_rules_from_history, get_apriori_recommendation

# Load batch data
df = pd.read_csv("data/food_batches_shibuya.csv")

# Load historical data for Apriori
rules = learn_rules_from_history("data/reroute_history.csv")

# Initialize blockchain log
log_path = "blockchain_log.json"
try:
    import os

    if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
        with open(log_path, "r") as f:
            blockchain = json.load(f)
    else:
        blockchain = []

except FileNotFoundError:
    blockchain = []

for _, row in df.iterrows():
    batch_id = row["BatchID"]
    food_type = row["FoodType"]
    temp = row["Temperature"]
    humidity = row["Humidity"]
    transit = row["TransitTimeHrs"]
    expiry = row["ExpiryHrs"]
    location = row["Location"]

    # Step 1: Evaluate Risk and Urgency
    risk = evaluate_risk(food_type, temp, humidity, transit)
    urgent = is_urgent(food_type, expiry)

    # Step 2: Semantic Match
    semantic_match = match_receiver(food_type, expiry, location)

    # Step 3: Apriori Recommendation
    apriori_match = get_apriori_recommendation(food_type, location, expiry, rules)

    # Step 4: Choose best receiver
    target = apriori_match if apriori_match in semantic_match else semantic_match[0]

    # Step 5: Create blockchain entry
    log_entry = {
        "BatchID": batch_id,
        "FoodType": food_type,
        "Location": location,
        "RiskLevel": risk,
        "Urgent": urgent,
        "RecommendedReceiver": target,
        "Timestamp": datetime.now().isoformat()
    }

    blockchain.append(log_entry)
    print(f"✅ {batch_id}: {food_type} rerouted to {target} (Risk: {risk})")

# Save blockchain log
with open(log_path, "w") as f:
    json.dump(blockchain, f, indent=2)
