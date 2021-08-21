import json
import os

# Globals
OUTPUT_FILE_ABS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "filtered_media.json"
)
media_list = []


def get_media_list(backup_folders, backup_location):
    """
    Processes the media.json file in instagram's backup.

    param backup_folders: a list of folders in the IG backup folder
    type backup_folders: list of strings
    param backup_location: absolute location of the backup folder, including the folder name
    type backup_location: string
    """
    global media_list

    for location in backup_folders:
        file_to_open = os.path.join(backup_location, location, "media.json")

        with open(file_to_open, "r") as media_file:
            media_json = json.loads(media_file.read())
            media_list.extend(media_json["photos"])


def filter_media_list(criteria):
    """
    Filters and outputs the filtered list.

    param criteria: a dictionary with the field to filter by and the data to filter by
    type criteria: dictionary with two keys - field and includes
    """
    filtered_list = [
        m for m in media_list if criteria["includes"] in m[criteria["field"]]
    ]
    ordered_list = sorted(filtered_list, key=lambda post: post["taken_at"])
    write_dict = {"photos": ordered_list}

    with open(OUTPUT_FILE_ABS, "w") as output_file:
        output_file.write(json.dumps(write_dict))


def get_user_input():
    """
    Gets the user's input for the backup locations and the filter criteria
    """
    # Example: <username>_<date>_part_<number>,<username>_<date>_part_<number>
    bup_locations = input(
        "Enter the list of folders within your instagram backup that have media.json files. Separate the files with comma (,):\n For Example: <username>_<date>_part_<number>,<username>_<date>_part_<number>\n"
    )
    backup_folders = bup_locations.split(",")
    # Example: /home/user/folder/backup/
    backup_location = input(
        "Enter the absolute location of the backup folder (including the name of it), with a / in the end:\n For Example: /home/user/folder/backup/\n"
    )
    criteria = {}
    # From: caption, taken_at, location, path
    criteria["field"] = input(
        "Enter the field you want to filter by:\n Options: caption, taken_at, location, path\n"
    )
    # Example: Trips
    criteria["includes"] = input("Enter the text the field should include:\n")

    return (backup_folders, backup_location, criteria)


if __name__ == "__main__":
    backup_folders, backup_location, criteria = get_user_input()
    get_media_list(backup_folders, backup_location)
    filter_media_list(criteria)
