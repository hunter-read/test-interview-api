from flask import Flask, request, jsonify
from database import Database

# creates a Flask application, named app
app = Flask(__name__)

# GM lookup endpoint.
# Query Parameters: username: str
# Returns Json of GM information.
@app.route("/gm", methods=['GET'])
def get_gm():
    username = request.args["username"]
    results = get_gm_from_username(username=username)
    if (results is None):
        return "Username not Found", 404
    return jsonify(results)

def get_gm_from_username(username: str):
    db = Database()
    #Query the username first. Return none if not found.
    results = db.query("SELECT username, image, number_reviews, lookup_count FROM gms WHERE username = ?", [username])
    if len(results) == 0:
        return None
    
    #Update the lookup count / TODO: should be done asyncronously
    db.save("UPDATE gms SET lookup_count = lookup_count + 1 WHERE username = ?", [username])
    db.close()
    
    #Results is a list of tuples
    gm = results[0]
    return {
        "username": gm[0],
        "image": gm[1],
        "number_reviews": gm[2],
        "lookup_count": gm[3] + 1
    }

# Popularity Endpoint
# Query Params: None
# Returns list of GM usernames in descending order of lookup
@app.route("/popularity", methods=['GET'])
def popularity():
    return jsonify(get_popularity())

def get_popularity():
    db = Database()
    results = db.query("SELECT username FROM gms WHERE lookup_count >= 0 ORDER BY lookup_count DESC", [])
    db.close()
    gms = list(sum(results, ())) #flatten list of tuples. From [(""), (""), ...] to ["", "", ...]
    return gms

# run the application
if __name__ == "__main__":
    app.run(debug=True)