import re
import json

def extract_json(input_string):
    match = re.search(r'\{.*\}', input_string, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    else:
        return {}
    
def extract_json_string(input_string):
    return json.dumps(extract_json(input_string), ensure_ascii=False, indent=4)