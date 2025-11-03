# logic/semantic_rules.py

from logic.food_ontology import food_ontology

def evaluate_risk(food_type, temp, humidity, transit_time):
    if food_type not in food_ontology:
        return "Unknown"
    
    info = food_ontology[food_type]
    risk_score = 0

    if temp > info["ideal_temp"] + 5:
        risk_score += 1
    if humidity > info["max_humidity"]:
        risk_score += 1
    if transit_time > 2:  # hours
        risk_score += 1

    if risk_score == 0:
        return "Low"
    elif risk_score == 1:
        return "Moderate"
    elif risk_score == 2:
        return "High"
    else:
        return "Critical"

def is_urgent(food_type, expiry_hrs):
    if food_type not in food_ontology:
        return False
    return expiry_hrs <= food_ontology[food_type]["urgency_threshold"]
