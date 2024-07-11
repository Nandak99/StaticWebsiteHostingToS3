import json
import csv
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_json_file> <output_csv_file>")
    sys.exit(1)

input_json_file = sys.argv[1]
output_csv_file = sys.argv[2]

with open(input_json_file, 'r') as f:
    data = json.load(f)

with open(output_csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write CSV header
    writer.writerow([
        'Target',
        'Class',
        'Type',
        'Title',
        'Severity',
        'Description',
        'Resolution'
    ])
    
    # Write CSV rows
    for result in data.get('Results', []):
        for vulnerability in result.get('Misconfigurations', []):
            writer.writerow([
                result.get('Target'),
                vulnerability.get('Class'),
                vulnerability.get('Type'),
                vulnerability.get('Title'),
                vulnerability.get('Severity'),
                vulnerability.get('Description'),
                vulnerability.get('Resolution')
            ])

print(f"CSV file '{output_csv_file}' has been created.")
