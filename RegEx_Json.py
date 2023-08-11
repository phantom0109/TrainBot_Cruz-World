import re
import json

input_dict = {
    "timestamp": 1680066635,
    "objectType": "map",
    "alias": "AAAA4455_BBBB9999_C11"
}

# Define regex pattern to match each part of alias
pattern = r'([A-Z]{4}\d{4})_([A-Z]{4}\d{4})_(\w+)'

# Extract parts from alias using regex
match = re.match(pattern, input_dict['alias'])
part_a, part_b, part_c = match.groups()

# Create new dictionary with extracted parts and original keys/values
output_dict = {
    **input_dict,
    'partA': part_a,
    'partB': part_b, # This is a comment
    'partC': part_c # This is a comment

}

print(json.dumps(output_dict, indent=4))

