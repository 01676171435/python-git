import json

data = {'name':'Bill',
        'age':55,
        'countr':'bangladehs'
        }

json_encoded_str = json.dumps(data)
print(json_encoded_str)
json_decode = json.loads(json_encoded_str)
print(json_decode)
