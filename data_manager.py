import json

DATABASE_FILE = "database.json"

# Load the data json file
def load_data() -> dict:
    """
    Load the data from the JSON file.

    This function reads the JSON file specified by `DATABASE_FILE`
    and returns the data as a dictionary.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)

def save_data(data: dict) -> None:
    """
    Save the data to the JSON file.

    This function writes the provided data to the JSON file specified 
    by `DATABASE_FILE`, formatting it with an indent for readability.

    Args:
        data (dict): The data to be saved in the JSON file.
    """
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Find the last cream used
def get_last_used(data: dict) -> str:
    """
    Find and return the name of the last cream used.

    This function iterates through the list of creams and 
    returns the name of the cream that has `use` set to `True`.

    Args:
        data (dict): The data containing the list of creams.

    Returns:
        str: The name of the last cream used.
    """
    for item in data:
        if item['use']:
            return f"The name of the last cream is: {item['name']}"
    return "No cream has been used yet."

# Update the cream used
def update_use(*, data: dict, new_cream_used: str) -> str:
    """
    Update the usage status of the creams and save the changes.

    This function sets the `use` status to `True` for the cream
    specified by `new_cream_used`, and sets the `use` status of 
    all other creams to `False`. The updated data is then saved
    to the JSON file.

    Args:
        data (dict): The data containing the list of creams.
        new_cream_used (str): The name of the cream that was last used.

    Returns:
        str: A message indicating which cream is now marked as used.
    """
    for item in data:
        if item['name'] == new_cream_used:
            item['use'] = True
        else:
            item['use'] = False
    save_data(data)
    return f"Updated! Now the last cream used is: {new_cream_used}"