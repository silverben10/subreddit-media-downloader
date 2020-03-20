#!/usr/bin/python3

import json
import sys
import os
import requests

user_agent = "subreddit-media-downloader by /u/silverben10"

# Parse arguments to catch any errors (e.g. no subreddit specified).
# TODO: Refactor this using `argparse`
try:
    subreddit = sys.argv[1]
except IndexError:
    print("Please include which subreddit you would like to pull images from.")
    sys.exit()

try:
    sort = sys.argv[2]
except IndexError:
    print("Please include which method you would like the sort the posts by.\n Options: new|best|hot|top")
    sys.exit()

try:
    top_time = sys.argv[3]
except:
    top_time = "all" if sort == "top" else ""

# Construct the url to pull the data from.
url = f"http://reddit.com/r/{subreddit}/{sort}/.json?raw_json=1&t="+top_time

# Perform the request and grab the content of the response (i.e. the posts)
r = requests.get(url, headers={"User-agent": user_agent})
response = json.loads(r.text)

# Create the directory to store the posts in (or don't, if it already exists).
try:
    os.mkdir(f"{subreddit}")
except FileExistsError:
    print("Directory already exists. Downloading content into it.")

print(f"Requesting data from {url}")

# Iterate through each post "containing" an image and download this image into the directory created above.
posts = response["data"]["children"]
for post in posts:
    # TODO: Perhaps isolate the posts with images by using filter() instead of a try except?
    try:
        if post["data"]["post_hint"] == "image":
            image_url = post["data"]["url"]
            image_content = requests.get(
                image_url, allow_redirects=True).content
            print("Downloading image...")
            image_title = image_url.rsplit("/", 1)[1]
            open(os.path.join(subreddit, image_title), "wb").write(image_content)
    except KeyError:
        pass

print("Download complete!")
