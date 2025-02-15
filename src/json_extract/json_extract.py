import re
import json

def extract_json(input_string):
    try:
        match = re.search(r'\{.*\}', input_string, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            return {}
    except json.JSONDecodeError:
        return {}
    except Exception as e:
        print(f"An error occurred 5001: {e}")
        return {}