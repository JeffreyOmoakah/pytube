
import requests
from pytube import YouTube
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Your code here
myVideo = YouTube("https://www.youtube.com/watch?v=oS8lASbvlpI")
myVideoStreams = myVideo.streams
print(myVideoStreams)