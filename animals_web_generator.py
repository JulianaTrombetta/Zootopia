import json


# Function to load JSON data from a file
def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Function to print animal data
def print_animal_data(animals_data):
    """Prints the specified fields for each animal."""
    for animal in animals_data:
        # Print the required fields if they exist
        if 'name' in animal:
            print(f"Name: {animal['name']}")
        if 'diet' in animal:
            print(f"Diet: {animal['diet']}")
        if 'locations' in animal and animal['locations']:
            print(f"Location: {animal['locations'][0]}")
        if 'type' in animal:
            print(f"Type: {animal['type']}")
        print()  # Blank line between animals for readability


# Main script execution
if __name__ == "__main__":
    # Load the data from the JSON file
    animals_data = load_data("animals_data.json")

    # Print the animal data
    print_animal_data(animals_data)
