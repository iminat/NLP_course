import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract specific information
employees = root.findall('employee')

# Iterate over employees and print their names and positions
for employee in employees:
    name = employee.find('name').text
    position = employee.find('position').text
    print(f"Name: {name}, Position: {position}")