import xml.etree.ElementTree as ET

# Function to recursively convert XML to HTML with dropdowns
def xml_to_html(element):
    # Skip the root 'tree' and 'link' elements from the HTML output
    if element.tag == 'tree' or (element.tag == 'link' and 'name' in element.attrib):
        # We simply skip over these elements and don't add them to the HTML
        children = list(element)
        html = ''
        for child in children:
            html += xml_to_html(child)  # Recursively process the children
        return html

    # Start the details block with the element's name (tag)
    html = f'<details><summary>{element.attrib.get("name", "")}</summary>'
    
    # If the element has text, display it (but strip out leading/trailing whitespace)
    if element.text and element.text.strip():
        html += f'<p>{element.text.strip()}</p>'
    
    # If the element has children (directories or files), recursively process them
    children = list(element)
    if children:
        html += '<ul>'  # Start an unordered list for the child elements
        for child in children:
            html += f'<li>{xml_to_html(child)}</li>'  # Recursively create a <li> for each child
        html += '</ul>'  # End the unordered list
    
    html += '</details>'  # Close the details block
    return html

# Function to parse the XML file and generate the HTML
def convert_xml_to_html(xml_file, output_html_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Convert the root element to HTML with dropdowns
    html_content = xml_to_html(root)
    
    # Wrap the HTML content in a basic HTML structure, including the converted XML content
    html_page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>XML to HTML with Dropdowns</title>
        <style>
            /* Remove bullet points from unordered lists */
            ul {{
                list-style-type: none; /* Removes default bullet points */
                padding-left: 0;       /* Remove left padding */
            }}
            details {{
                margin-bottom: 10px;
            }}
            summary {{
                font-weight: bold;
                cursor: pointer;
            }}
            li {{
                margin-left: 20px;  /* Indentation for nested items */
            }}
            p {{
                margin-left: 20px;
            }}
        </style>
    </head>
    <body>
        {html_content}  <!-- Insert the generated HTML content here -->
    </body>
    </html>
    """
    
    # Write the HTML content to the output file
    with open(output_html_file, 'w') as file:
        file.write(html_page)
    
    print(f"HTML content has been saved to {output_html_file}")

# Example usage
# input_xml_file = 'full_module_tree.xml'  # Replace with the path to your XML file
input_xml_file = 'temp.xml'  # Replace with the path to your XML file
output_html_file = 'output.html'  # Output HTML file

# Convert the XML to HTML
convert_xml_to_html(input_xml_file, output_html_file)

