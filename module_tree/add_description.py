import xml.etree.ElementTree as ET

# Step 1: Parse the XML file
tree = ET.parse('temp.xml')  # Replace 'items.xml' with your XML file
root = tree.getroot()

# Step 2: Iterate through all <item> elements
for item in root.findall('item'):
    # Check if the <file> element exists and is empty
    file_element = item.find('file')
    if file_element is not None and file_element.text == '':
        # Step 3: Create a new <paragraph> element
        paragraph = ET.Element('paragraph')
        paragraph.text = 'This is a new paragraph.'  # You can customize the text content
        item.append(paragraph)  # Append the new paragraph to the current item

# Step 4: Save the modified XML
tree.write('modified_items.xml')  # Save to a new file or overwrite

