import fresh_tomatoes
import webbrowser

#Contains the data and methnods necessary to render a single move on
#the Movie Trailer Website by fresh_tomatoes.py
class Movie():
    def __init__(self, title, storyline, img_url, youtube_url):
        #movie title
        self.title = title
        #short description of the movie
        self.storyline = storyline
        #url of the image used to represent the move
        self.poster_image_url = img_url
        #url of the youtube video showing the movie's trailer
        self.trailer_youtube_url = youtube_url

    #opens a browser window playing the movie's trailer video
    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)

#list of Movies to be used on the webpage
movies = [Movie("Frozen",
                "Two sisters separated by chilling misfortune",
                "https://b-i.forbesimg.com/scottmendelson/files/2013/11/Frozen-movie-poster.jpg",
                "https://www.youtube.com/watch?v=TbQm5doF_Uc"),
          Movie("Finding Nemo",
                "A father clown-fish's search for his lost son couldn't be more enjoyable",
                "http://www.goldenglobes.com/sites/default/files/films/finding_nemo.jpeg",
                "https://www.youtube.com/watch?v=w2-Jrglx2BM"),
          Movie("Rat Race",
                "Two million dollars is enough to make anyone act crazy",
                "https://images-na.ssl-images-amazon.com/images/I/51lZj1Ef8oL.jpg",
                "https://www.youtube.com/watch?v=ekqud8M4xLk")]

#open the webpage--passing it he above list of movies to dieplay
fresh_tomatoes.open_movies_page(movies)
