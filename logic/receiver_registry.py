# logic/receiver_registry.py

receiver_registry = {
    "Ebisu": {
        "Sakura Café": ["Bento", "Sandwich"],
        "Smile Food Bank": ["All"]
    },
    "Daikanyama": {
        "Little Bento Shop": ["Bento", "Onigiri"],
        "Tokyu Store Mini Market": ["Bento", "Milk", "Onigiri"]
    },
    "Harajuku": {
        "Harajuku High School": ["Milk", "Sandwich"]
    },
    "Yoyogi": {
        "Shibuya Tech Office": ["Sandwich", "Onigiri"]
    }
}

def match_receiver(food_type, expiry_hrs, location):
    matched = []

    loc_receivers = receiver_registry.get(location, {})
    for receiver, accepted in loc_receivers.items():
        if food_type in accepted or "All" in accepted:
            if expiry_hrs < 3 or "Food Bank" in receiver:
                matched.append(receiver)

    return matched if matched else ["No match"]
