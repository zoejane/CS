import webbrowser

class Movie():
    def  __init__(self, movie_title, movie_storyline, poster_image,
                  trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Music():
    def __inti__(self,
                 music_title, music_album, music_artist,
                 artist_photo, album_photo,
                 song_url):
        self.title = music_title
        self.album = music_album
        self.artist = music_artist
        self.artist_photo = artist_photo
        self.album_photo = album_photo
        self.song_url = song_url
    
