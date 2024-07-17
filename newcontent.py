import json
import os

def get_game_details():
    details = {}

    description = input("Enter the description (optional): ")
    if description:
        details['description'] = description

    details['id'] = input("Enter the ID: ")
    details['name'] = input("Enter the name: ")

    publisher = input("Enter the publisher (optional): ")
    if publisher:
        details['publisher'] = publisher

    region = input("Enter the region (optional): ")
    if region:
        details['region'] = region

    release_date = input("Enter the release date (YYYYMMDD): ")
    details['releaseDate'] = int(release_date)

    size = input("Enter the size (in bytes) (optional): ")
    if size:
        details['size'] = int(size)

    version = input("Enter the version: ")
    details['version'] = int(version)

    return details

def save_game_details(directory, game_details):
    file_path = os.path.join(directory, f"{game_details['id']}.json")
    with open(file_path, 'w') as json_file:
        json.dump(game_details, json_file, indent=4)
    print(f"Details saved to {file_path}")

def update_game_details(file_path):
    with open(file_path, 'r') as json_file:
        game_details = json.load(json_file)

    print(f"Current details: {json.dumps(game_details, indent=4)}")

    new_description = input(f"Enter the description (current: {game_details.get('description', 'None')}): ")
    if new_description:
        game_details['description'] = new_description

    new_name = input(f"Enter the name (current: {game_details['name']}): ")
    if new_name:
        game_details['name'] = new_name

    new_publisher = input(f"Enter the publisher (current: {game_details.get('publisher', 'None')}): ")
    if new_publisher:
        game_details['publisher'] = new_publisher

    new_region = input(f"Enter the region (current: {game_details.get('region', 'None')}): ")
    if new_region:
        game_details['region'] = new_region

    new_release_date = input(f"Enter the release date (YYYYMMDD) (current: {game_details['releaseDate']}): ")
    if new_release_date:
        game_details['releaseDate'] = int(new_release_date)

    new_size = input(f"Enter the size (in bytes) (current: {game_details.get('size', 'None')}): ")
    if new_size:
        game_details['size'] = int(new_size)

    new_version = input(f"Enter the version (current: {game_details['version']}): ")
    if new_version:
        game_details['version'] = int(new_version)

    with open(file_path, 'w') as json_file:
        json.dump(game_details, json_file, indent=4)
    print(f"Details updated in {file_path}")

def main():
    content_types = {
        1: 'base',
        2: 'dlc',
        3: 'update'
    }

    print("Select the type of content you want to add:")
    print("1. Base")
    print("2. DLC")
    print("3. Update")
    choice = int(input("Enter the number corresponding to your choice: "))

    content_type = content_types.get(choice)
    if not content_type:
        print("Invalid choice. Exiting.")
        return

    directory = content_type
    os.makedirs(directory, exist_ok=True)

    game_id = input("Enter the ID of the game: ")
    file_path = os.path.join(directory, f"{game_id}.json")

    if os.path.exists(file_path):
        print(f"{file_path} already exists.")
        update_game_details(file_path)
    else:
        print(f"{file_path} does not exist. Creating new file.")
        game_details = get_game_details()
        game_details['id'] = game_id  # Ensure the ID is consistent
        save_game_details(directory, game_details)

if __name__ == "__main__":
    main()