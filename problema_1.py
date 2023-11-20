# Create a function that checks the data in a list of dictionaries for specific validation rules, like checking if certain columns are non-empty, if numbers are within a range, etc.

data = [
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': '', 'email': 'bob@example.com'},  # Bob are certificat de nastere, totu bine, doar au uitat astia sa puna varsta ;)
    {'name': '', 'age': 20, 'email': 'carol@example.com'},   # Numele e uitat intentionat ;)
    {'name': 'Dave', 'age': 200, 'email': 'dave@example.com'} # Dave e world record pt cel mai batran om
]

validation_rules = {
    'name': {'required': True, 'type': str},
    'age': {'required': True, 'type': int, 'min': 0, 'max': 120},
    'email': {'required': True, 'type': str}
}

def validate_data(data, validation_rules):
    for item in data:
        item_validation = True
        for key,val in item.items():
            rules = validation_rules[key]
            valid = type(val) == rules['type']
            valid = valid and (bool(val) if rules['required'] else True)
            valid = valid and (val<rules['max'] if 'max' in rules else True)
            valid = valid and (val > rules['min'] if 'min' in rules else True)
            item_validation = item_validation and valid
        message = f"validation complete for {item=}" if item_validation else f"validation failed for {item=}"
        print(message)

validate_data(data, validation_rules)




