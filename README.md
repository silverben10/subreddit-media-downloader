# subreddit-media-downloader
A CLI tool for downloading all media posts from a given subreddit (or as many as possible).

## How to use
1. Clone this repository using the following command:
```
git clone https://github.com/silverben10/subreddit-media-downloader.git
```

2. `cd` into the newly created repository:
```
cd subreddit-media-downloader
```

3. Run `main.py` in the command line, passing in the required arguments (detailed below):
```
python main.py [subreddit] [sort] [top timeframe]
```

4. The script will then download the images returned by Reddit and save them in a folder named after the subreddit.

## Arguments
### `subreddit`
The subreddit you want to download images from. This'll work best on image-heavy subreddits (e.g. */r/wallpapers*, */r/pics*).

### `sort`
The order you want the subreddit's posts to be sorted by before they are returned. This will affect the images downloaded, since sorting by `new` will return different posts to sorting by `top`.

**Values:** `new|best|hot|top`

*Note:* If you plan to sort by `top`, please include one of the `top timeframe` arguments below. Otherwise, `top` will default to the `all` timeframe.

### `top timeframe`
The timeframe within which to grab the top posts on the subreddit.

**Values:** `hour|day|week|month|year|all`

***

That's pretty much it!