import json
import csv

def json_to_csv():
    # Prompt for the JSON file path
    json_file = input("Enter the path to the JSON file: ")

    try:
        # Open the JSON file and load its contents
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return

    # Extract the keys from the first object in the JSON data
    keys = data[0].keys()

    # Prompt for the CSV file name
    csv_file = input("Enter the name of the CSV file (without extension): ") + ".csv"

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV conversion complete. Saved as {csv_file}.")

# Call the function to convert JSON to CSV
json_to_csv()
