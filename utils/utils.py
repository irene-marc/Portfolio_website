import json


def read_json(file_path):
    """
    Reads a JSON file and returns its content as a dictionary.
    
    Parameters:
    - file_path: str, path to the JSON file.
    
    Returns:
    - dict, content of the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file at {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")