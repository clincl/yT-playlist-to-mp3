
# yT playlist to mp3

> From Youtube Playlist to mp3 files.

This project scrapes a youtube playlist's urls into a csv file. The urls are then used to download the videos in mp3 format.
APIS Used

## APIs Used
- <a href="https://developers.google.com/youtube/v3"> Youtube Data API </a>
- <a href="https://github.com/ytdl-org/youtube-dl">Youtube dll API</a>

## Installation

### Clone
- Start by cloning the repo.
```shell
$ git clone https://github.com/clincl/yT-playlist-to-mp3
$ cd yT-playlist-to-mp3
```
### Setup
- You will need to create and setup a config.py file.
- Activate the Youtube Data API and get your key from the <a href="https://console.developers.google.com/projectselector2/apis/dashboard?supportedpurview=project">Google Developers Console</a>.
- Your pID or playlist ID can be found in the 'list' parameter in a youtube url. For example, `https://www.youtube.com/playlist?list=pID`.
- Once you have everything, your config.py should look something like this:
```shell
api_key = YOUR_API_KEY
pId = YOUR_YOUTUBE_PLAYLIST_ID
```

## Usage
```shell
$ python write.py
$ python download.py
```

## Notes
- `download.py` doesn't account for some errors. I didn't test for them but these likely deal with deleted/private videos. 
- My work around was to manually delete the lines up to the error and run `python download.py` again.

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
- Copyright 2019 © Chuan Lin.