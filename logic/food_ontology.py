# logic/food_ontology.py

food_ontology = {
    "Bento": {
        "category": "PreparedMeal",
        "ideal_temp": 10,
        "max_humidity": 75,
        "urgency_threshold": 3  # hours
    },
    "Onigiri": {
        "category": "Snack",
        "ideal_temp": 15,
        "max_humidity": 80,
        "urgency_threshold": 4
    },
    "Sandwich": {
        "category": "ColdFood",
        "ideal_temp": 8,
        "max_humidity": 70,
        "urgency_threshold": 3
    },
    "Milk": {
        "category": "Dairy",
        "ideal_temp": 5,
        "max_humidity": 70,
        "urgency_threshold": 6
    }
}
