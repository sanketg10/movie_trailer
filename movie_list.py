# This file presents all the different movies which have been created using Movie class
# This Movie class is imported from movies.py and then sent to fresh_tomatoes.py for creating html file
# The Movie object contains title, story, poster_image, youtube URL to be
# displayed in the file

import movies
import fresh_tomatoes

bajrangi_bhaijaan = movies.Movie("Bajrangi Bhaijaan", "A story of redemption and love",
                                 "https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg",
                                 "https://www.youtube.com/watch?v=vyX4toD395U")

star_wars = movies.Movie("Star Wars", "A story of a colony deep within the stars...",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                         "https://www.youtube.com/watch?v=1g3_CFmnU7k")

sultan = movies.Movie("Sultan", "A story of wrestler and his dream",
                      "http://data1.ibtimes.co.in/cache-img-600-0-photo/en/full/41514/1467886188_salman-khan-anushka-sharmas-sultan-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=i0xPsUOlnmY")

gladiator = movies.Movie("Gladiator", "A story of a gladiator and his freedom",
                         "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                         "https://www.youtube.com/watch?v=owK1qxDselE")

twelve_angry_men = movies.Movie("12 Angry Men", "A story of impossible convicing power of a single man",
                                "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
                                "https://www.youtube.com/watch?v=fSG38tk6TpI")

finding_nemo = movies.Movie("Finding Nemo", "A story of a cute fish",
                            "http://assets.fontsinuse.com/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0",
                            "https://www.youtube.com/watch?v=wZdpNglLbt8")

shock_awe = movies.Movie("Shock and Awe", "Story of Electricity",
                         "https://i.jeded.com/i/bbc-shock-and-awe-the-story-of-electricity.7642.jpg",
                         "https://www.youtube.com/watch?v=Gtp51eZkwoI")

meru = movies.Movie("Meru", "Story of impossible climb made possible",
                    "https://loftcinema.com/files/2015/07/meru-poster.jpg",
                    "https://www.youtube.com/watch?v=qdWzTqyMtSU")

queen = movies.Movie("Queen", "Story of impossible climb made possible",
                     "http://st1.bollywoodlife.com/wp-content/uploads/2014/03/motion-poster1.jpg",
                     "https://www.youtube.com/watch?v=KGC6vl3lzf0")

movie_list = [sultan, star_wars, bajrangi_bhaijaan, shock_awe, meru, queen,
              gladiator, twelve_angry_men, finding_nemo]

# Sending the movie_list to fresh_tomatoes which has the function
# open_movies_page
fresh_tomatoes.open_movies_page(movie_list)
