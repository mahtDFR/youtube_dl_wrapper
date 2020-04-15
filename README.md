wrapper script for use with [youtube-dl](https://github.com/ytdl-org/youtube-dl).

requires python 3 and youtube-dl must be added to PATH. see their repo for more details.

[yt-dl-wrapper.py](https://github.com/mahtDFR/youtube_dl_wrapper/blob/master/yt-dl-wrapper.py) wraps youtube-dl into an infinite loop so it doesn't have to be repeatedly called in a terminal if you have a lot of links to process. just paste links that include video content from youtube, vimeo, twitter, instagram, bbc-iplayer, etc. and it will download video as mp4 into the script directory. currently video downloads happen one-by-one, but this could be adapted.

the script uses no arguments when calling youtube-dl so default encoding settings are used.


