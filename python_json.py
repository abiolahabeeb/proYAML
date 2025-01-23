import json
# Simple Dictionary
employee_01 = {
    "name": "Martin",
    "job": "Developer",
    "Skill": "ELite",
    "employed": True,
}
print(type(employee_01)) # <class 'dict'>

#Serializing
json_object = json.dumps(employee_01)
print(json_object)
print(type(json_object))