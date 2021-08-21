import json
import os

# Globals
OUTPUT_FILE_ABS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "filtered_media.json"
)
media_list = []


def get_media_list(backup_location):
    """
    Processes the media.json file in instagram's backup.

    param backup_location: absolute location of the backup folder, including the folder name
    type backup_location: string
    """
    global media_list

    file_to_open = os.path.join(backup_location, "content/posts_1.json")

    with open(file_to_open, "r") as media_file:
        media_json = json.loads(media_file.read())
        media_list.extend(media_json)


def filter_media_list(criteria):
    """
    Filters and outputs the filtered list.

    param criteria: a dictionary with the field to filter by and the data to filter by
    type criteria: dictionary with two keys - field and includes
    """
    filtered_list = [
        m
        for m in media_list
        if criteria["includes"] in m["media"][0][criteria["field"]]
    ]
    ordered_list = sorted(filtered_list, key=lambda post: post["media"][0]["creation_timestamp"])
    write_dict = {"photos": ordered_list}

    with open(OUTPUT_FILE_ABS, "w") as output_file:
        output_file.write(json.dumps(write_dict))


def get_user_input():
    """
    Gets the user's input for the backup locations and the filter criteria
    """
    # Example: /home/user/folder/backup/
    backup_location = input(
        "Enter the absolute location of the backup folder (including the name of it), with a / in the end:\n For Example: /home/user/folder/backup/\n"
    )
    criteria = {}
    # From: uri, creation_timestamp, title
    criteria["field"] = input(
        "Enter the field you want to filter by:\n Options: uri, creation_timestamp, title\n"
    )
    # Example: Trips
    criteria["includes"] = input("Enter the text the field should include:\n")

    return (backup_location, criteria)


if __name__ == "__main__":
    backup_location, criteria = get_user_input()
    get_media_list(backup_location)
    filter_media_list(criteria)
