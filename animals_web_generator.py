import json


# Function to load JSON data from a file
def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Function to generate a string with the animals' data
def generate_animals_info(animals_data):
    """Generates a formatted string with animal information."""
    output = ''
    for animal in animals_data:
        if 'name' in animal:
            output += f"Name: {animal['name']}<br>\n"
        if 'diet' in animal:
            output += f"Diet: {animal['diet']}<br>\n"
        if 'locations' in animal and animal['locations']:
            output += f"Location: {animal['locations'][0]}<br>\n"
        if 'type' in animal:
            output += f"Type: {animal['type']}<br>\n"
        output += "<br>\n"  # Add a blank line between animals
    return output


# Function to generate HTML content
def generate_html(template_path, output_path, animals_info):
    """Replaces the placeholder in the HTML template with the animals' information."""
    # Read the HTML template
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    # Debug: Print the template content
    print("Template Content:")
    print(template_content)

    # Replace the placeholder with the animals' information
    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Debug: Print the updated content
    print("Updated HTML Content:")
    print(updated_content)

    # Write the updated content to the new HTML file
    with open(output_path, "w") as output_file:
        output_file.write(updated_content)


# Main script execution
if __name__ == "__main__":
    # Load the animal data
    animals_data = load_data("animals_data.json")

    # Generate the animals' information string
    animals_info = generate_animals_info(animals_data)
    print("Generated Animals Info:")
    print(animals_info)  # Debug: Print the generated animals' information

    # Generate the updated HTML file
    generate_html("animals_template.html", "animals.html", animals_info)

    print("HTML file 'animals.html' has been generated successfully.")
