import os
import csv

def load_data(file_path, object_type=None):
    """Load data from file into a list of dictionaries or list of objects."""
    data = []
    try:
        with open(os.path.join('database', file_path), mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if object_type:
                    # Convert dict to object
                    data.append(object_type(**row))
                else:
                    data.append(dict(row))
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while loading data from {file_path}: {e}")
    return data

def save_data(file_path, data):
    """Save data to file, taking list of dictionaries or list of objects and saving it to file."""
    if len(data) == 0:
        print(f"Error: No data to save to {file_path}.")
        return

    # Check if data is a list of objects and convert to dict
    if hasattr(data[0], 'to_dict'):
        data = [item.to_dict() for item in data]

    # Get the path to the file
    full_path = os.path.join('database', file_path)

    with open(full_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for item in data:
            writer.writerow(item)
