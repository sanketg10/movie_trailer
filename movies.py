#This file defines the Movie class which is used in movie_list.py to create different movie objects
import webbrowser

class Movie:
    def __init__(self,title,story,poster_image,trailer_youtube_url):
        self.title = title
        self.story = story
        self.poster_image = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def open_trailer(self,trailer_youtube_url):
        webbrowser.open(self.trailer_youtube_url)