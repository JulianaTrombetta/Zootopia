import json


# Function to load JSON data from a file
def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Function to serialize a single animal into HTML
def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    # Access nested fields for diet and type
    characteristics = animal_obj.get("characteristics", {})
    output += f'    <strong>Diet:</strong> {characteristics.get("diet", "Unknown")}<br/>\n'
    output += f'    <strong>Location:</strong> {animal_obj["locations"][0] if "locations" in animal_obj and animal_obj["locations"] else "Unknown"}<br/>\n'
    output += f'    <strong>Type:</strong> {characteristics.get("type", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


# Function to generate a string with the animals' data as styled HTML list items
def generate_animals_info(animals_data):
    """Generates a formatted string with all animals serialized into HTML list items."""
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


# Function to generate HTML content
def generate_html(template_path, output_path, animals_info):
    """Replaces the placeholder in the HTML template with the animals' information."""
    # Read the HTML template
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with the animals' information
    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write the updated content to the new HTML file
    with open(output_path, "w") as output_file:
        output_file.write(updated_content)


# Main script execution
if __name__ == "__main__":
    # Load the animal data
    animals_data = load_data("animals_data.json")

    # Debug: Print the loaded JSON data structure
    print("Loaded JSON Data:")
    print(json.dumps(animals_data, indent=4))

    # Generate the animals' information string as styled HTML list items
    animals_info = generate_animals_info(animals_data)
    print("Generated Animals Info as HTML:")
    print(animals_info)  # Debug: Print the generated HTML for animals

    # Generate the updated HTML file
    generate_html("animals_template.html", "animals.html", animals_info)

    print("HTML file 'animals.html' has been generated successfully.")
