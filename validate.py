import json
import jsonschema 
from jsonschema import validate

#expected json schema
StudentSchema = {
    "type" : "object",
    "properties" : {
        "Name" : {
            "type" : "string"
        },
        "Age" : {
            "type": "integer",
            "minimum" : 10
        },
        "Faculty" : {
            "type" : "string"
        }
    },
    "required" : ["Name", "Age"]
}

# dictionary for holding data
dict = {
    'Name' : 'Jivan Dhamala',
    'Age' : 23,
}

#function for validating dictionary with jsonschema
def validateJSON(dict, jsonSchema):
    try:
        validate(instance=dict, schema=jsonSchema)

    except jsonschema.exceptions.ValidationError as err:
        return False

    return True

# converting json to python dictionary object
#jsonData = json.loads('json_file')

isValid = validateJSON(dict, StudentSchema)
print(isValid)