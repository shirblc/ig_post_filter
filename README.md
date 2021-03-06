# Instagram Post Filter

A Python script to filter the posts as found in the Instagram JSON backup. The script fetches all the JSON files you give it and returns only the posts matching the given criteria.

## Requirements

1. Python 3
2. Instagram backup in JSON format (Under settings -> security and privacy -> request data, choose JSON)
  - You'll need to get the names of all the subfolders that contain a `media.json` file
  - You'll need the **full path** of the backup folder, for example: /home/user/documents/<ig_username>_<download_date>/

## Installation and Usage

1. Clone/download the repo
2. In your terminal, cd into the repo.
3. Choose the script to run, depending on your backup:
  - If you're filtering a 2020 or earlier backup, use `python filter_instagram_posts.py` (or `python3 filter_instagram_posts.py` on macOS).
  - If you're filtering a newer backup, use `python filter_instagram_data_2021.py` (or `python3 filter_instagram_data_2021.py` on macOS).
  - If you're running into issues with either, try the other script. The dates above aren't exact (the earlier script was built using a 2020 backup and the 2021 script was built using a 2021 backup).
4. Fill the required details.

## Known Issues

There are no known issues at this time.
