# Movie Trailer

**Overview:**

This app shows all my favorite movie sites :) It is configured as a Flask application that renders the `fresh_tomatoes.html` inside the `templates` folder.

**Seeing the final site:**

1. Go to `someideastoshare.xyz` to access the site OR
2. Go to `fresh_tomatoes.html` inside the `templates` folder to access the same site.

**Architecture:**

1. `movies.py` is the file where `Movie` class is defined and whose objects will be created for rendering.
2. `movie_list.py` is the file where all the `Movie` objects are created and the function from `fresh_tomatoes.py` to create the html page is called.
3. `fresh_tomatoes.py` is the file which creates the `fresh_tomatoes.html` inside the `templates` folder.

**Running as a Flask app:**

1. First set up the virtual environment using `. ./movie_trailer/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run the python file using `python movie_list.py`. This will create the html file in `templates` folder.
4. Run `python app.py`. This will start the site on the local host.
5. This Flask app has been deployed using Heroku and the custom domain used is `someideastoshare.xyz` which was bought on Namecheap
