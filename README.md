wrapper script for use with youtube-dl.

requires [youtube-dl](https://github.com/ytdl-org/youtube-dl) and python 3 to use.
youtube-dl must be added to the PATH variable. see their repo for more details.

this script wraps youtube-dl into an infinite loop so it doesn't have to be repeatedly called in a terminal if you have a lot of links to process. just paste links from youtube, vimeo, twitter, etc. and it will download video as mp4. currently this only works in series. it could be adapted to input multiple links at once.

the script uses no arguments so default youtube-dl settings are used.


