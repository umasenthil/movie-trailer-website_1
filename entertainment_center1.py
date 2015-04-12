import media
import fresh_tomatoes
import urllib
import urllib2
import json

# Adding favorite movie list
movie_list = ("Gandhi", "Lincoln", "Apollo 13", "The Shawshank Redemption")

#Create empty list to store all movie details
movie_details = []

#Populate the movie_details from querying the information from a website.
for each in movie_list:
    output = each
    if ' 'in each:
        output = each.replace(' ', '+')
        
    response = urllib2.urlopen("http://www.omdbapi.com/?t="+output+"&y=&plot=short&r=json")
    the_page = response.read()
	
    data = json.loads(the_page)
    movie_details.append(data)


# create Movie instances
gandhi = media.Movie(movie_details[0]["Title"],
                     movie_details[0]["Plot"],
                     "http://upload.wikimedia.org/wikipedia/en/1/10/Gandhi-poster.png",
                     "https://www.youtube.com/watch?v=CZVsWzIb6Vk",
                     movie_details[0]["Released"],
                     movie_details[0]["Actors"])
lincoln = media.Movie(movie_details[1]["Title"],
                      movie_details[1]["Plot"],
                      "http://upload.wikimedia.org/wikipedia/en/6/6a/Lincoln_2012_Teaser_Poster.jpg",
                      "https://www.youtube.com/watch?v=KJVuqYkI2jQ",
                      movie_details[1]["Released"],
                      movie_details[1]["Actors"])
apollo_13 = media.Movie(movie_details[2]["Title"],
                        movie_details[2]["Plot"],
                        "http://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                        "https://www.youtube.com/watch?v=KtEIMC58sZo",
			movie_details[2]["Released"],
                        movie_details[2]["Actors"])
shawshank_redemption = media.Movie(movie_details[3]["Title"],
				movie_details[3]["Plot"],
                                "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                "https://www.youtube.com/watch?v=6hB3S9bIaco",
				movie_details[3]["Released"],
                                movie_details[3]["Actors"])

# Put all the movie instances in a tuple.
movies = (gandhi, lincoln, apollo_13, shawshank_redemption)

# Call the open_movies_page module and pass the movies tuple with movie instances
fresh_tomatoes.open_movies_page(movies)
