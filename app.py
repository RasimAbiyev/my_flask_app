# app.py

from flask import Flask, render_template, request
from config import Config
from extensions import db
from models import Movie
import requests
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_title = request.form.get('title')
    api_key = '73013335'
    
    url = f'http://www.omdbapi.com/?t={movie_title}&apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        
        movie = Movie(
            title=movie_data.get('Title'),
            year=movie_data.get('Year'),
            rated=movie_data.get('Rated'),
            released=movie_data.get('Released'),
            runtime=movie_data.get('Runtime'),
            genre=movie_data.get('Genre'),
            director=movie_data.get('Director'),
            writer=movie_data.get('Writer'),
            actors=movie_data.get('Actors'),
            plot=movie_data.get('Plot'),
            language=movie_data.get('Language'),
            country=movie_data.get('Country'),
            awards=movie_data.get('Awards'),
            poster=movie_data.get('Poster'),
            metascore=movie_data.get('Metascore'),
            imdb_rating=movie_data.get('imdbRating'),
            imdb_votes=movie_data.get('imdbVotes'),
            imdb_id=movie_data.get('imdbID')
        )
        
        db.session.add(movie)
        db.session.commit()
        
        return f"Movie '{movie.title}' added to the database!"
    else:
        return f"Error: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)

    # api_key = '73013335'