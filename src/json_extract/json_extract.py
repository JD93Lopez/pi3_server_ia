import re
import json

def extract_json(input_string, error_value):
    try:
        match = re.search(r'\{.*\}', input_string, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            return error_value
    except json.JSONDecodeError:
        return error_value
    except Exception as e:
        print(f"An error occurred 5001: {e}")
        return error_value