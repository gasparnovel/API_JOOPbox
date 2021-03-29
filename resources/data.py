from jsonschema import validate
import json


class Data():

    # data.json
    datos = {
        "data": [
            {
                "name": "Jhon Snow",
                "id": "12345678-Z",
                "phone_number": 600000000,
                "street_name": "JSON square 12",
                "street_type": "Square"
            },
            {
                "name": "Jean Doe",
                "id": "X7654321-J",
                "phone_number": 616000000,
                "street_name": "python's exception 23, 1",
                "street_type": "Street",
                "birth_date": "1995-12-12",
                "food_preferences": "Vegan"
            },
            {
                "name": "Alex Dotcom",
                "id": "17283946-K",
                "phone_number": 34619000000,
                "street_name": "Java Class 7, 8",
                "street_type": "Avenue",
                "birth_date": "1998-04-03",
                "interests": ["work", "jobs", "production"]
            },
            {
                "name": "Dr. X",
                "id": "00000000-X",
                "phone_number": 609000000,
                "street_name": "PHP spaguetti code 169, 5",
                "street_type": "Boulevard",
                "birth_date": "1984-11-01",
                "interests": "Rule the world"
            }
        ]
    }

    # schema.json
    schema = {
        "type": "object",
        "properties": {
            "name":     {"type": "string"},
            "id":       {"type": "string"},
            "phone_number": {"type": "number"},
            "street_name":  {"type": "string"},
            "street_type":  {
                "type": "string",
                "enum": ["Street", "Avenue", "Boulevard", "Square", "Other"]
            },
            "birth_date":  {"type": "string"},
            "email":  {"type": "string"},
            "interests": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["name", "id", "phone_number"],
        "additionalProperties": False
    }