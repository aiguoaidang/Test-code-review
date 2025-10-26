import csv
import json

def convert_csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        # This is a code smell: reading the whole file into memory
        for row in reader:
            data.append(row)

    # This is another code smell: hardcoded header
    header = data[0]
    data = data[1:]

    json_data = []
    for row in data:
        json_row = {}
        for i in range(len(header)):
            # This is a potential bug: assumes all rows have the same number of columns as the header
            json_row[header[i]] = row[i]
        json_data.append(json_row)

    with open(json_file, 'w') as f:
        # This is a code smell: not using a context manager for writing
        json.dump(json_data, f, indent=4)

if __name__ == '__main__':
    # This is a code smell: hardcoded file paths
    convert_csv_to_json('e:\\开发文档\\202510\\26 KCA\\test-code-review\\data.csv', 'e:\\开发文档\\202510\\26 KCA\\test-code-review\\data.json')