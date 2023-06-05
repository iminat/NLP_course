import json

# Read JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Extract specific information
employees = data['employees']

# Iterate over employees and print their names and positions
for employee in employees:
    name = employee['name']
    position = employee['position']
    print(f"Name: {name}, Position: {position}")