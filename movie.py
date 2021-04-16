from flask import Flask , jsonify
app = Flask(__name__)



Movies = [{'Title':"Sonic The Hedgehog",
           'Movie_id':"1",
           'Duration': "1h 40minutes",
           'Genre': "Animation, Comedy, Adventure, Fantasy"},
           {'Title':"The Old Guard",
            'Movie_id':"2",
            'Duration':"2h 5minutes",
            'Genre':"Action, Fantasy, Superhero"},
           {'Title':"Blended",
            'Movie_id':"3",
            'Duration':"1h 57minutes",
            'Genre':"Romantic Comedy"}

         ]

@app.route('/')
def index():
    return "Welcome To My Movie Library"

 @app.route("/Movies",methods=['GET'])
 def get_movie():
     return jsonify({'Movies':Movies})

# @app.route("/Movies/<int:Movie_id>",methods=['GET'])
# def get_movieId(Movie_id):
#     return jsonify({'Movies':Movies[Movie_id]})

# @app.route("/Movies/<string:Title>",methods=['GET'])
# def get_movieTitle(Title):
#     return jsonify({'Movies':Movies[Title]})

# @app.route("/Movies/<string:Genre>",methods=['GET'])
# def get_movieGenre(Genre):
#     return jsonify({'Movies':Movies[Genre]})

# @app.route("/Movies/<string:Duration>",methods=['GET'])
# def get_movieDuration(Duration):
#     return jsonify({'Movies':Movies[Duration]})

# @app.route("/Movies",methods=['POST'])
# def create():
#     Movie = {'Title':"War Room", 
#               'Movie_id':"4",
#               'Duration':"2hrs",
#               'Genre':"Drama"
#               }
#     Movies.append(Movie)
#     return jsonify({'Created':Movie})

# @app.route("/Movies/<string:Movie_id>",methods=['PUT'])
# def updateMovie(Movie_id):
#     Movies['Movie_id']['Genre'] = "Christian Drama"
#     return jsonify({'Movies':Movies['Movie_id']})


# @app.route("/Movies/<string:Movie_id>",methods=['DELETE'])
# def delete():
#     Movies.remove(Movies[Movie_id])
#     return jsonify({'result':True})


# if __name__ == "__main__":

#     app.run(debug=True)

