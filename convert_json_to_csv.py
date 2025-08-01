import json
import csv

# Open the JSON file
with open('factory_data.json', 'r') as f:
    data = json.load(f)

# Ensure it's a list
if isinstance(data, dict):
    data = [data]

# Open a CSV file to write
with open('factory_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'temperature', 'humidity', 'device']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print("✅ JSON successfully converted to CSV.")


