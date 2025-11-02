from flask import Flask, jsonify, request
from models import db, Streamers
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/FENIX/Documents/CODE_VISUAL/PROYECTOS_PY/inter/Apy_rest/database/streamers.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#RUTAS---------------
#----------------------------------
@app.route("/")
def home():
    return "<h1>Welcome home </h1>"
#----------------------------------
@app.route("/api/streamers",methods=["GET"])#solo metodo get
def getStreamers():
    try:
        streamers = Streamers.query.all()
        toReturn = [streamer.serialize() for streamer in streamers]
        return jsonify(toReturn), 200
    except Exception:
        exception("error")
        return jsonify({"smg":"ha ocurrido un error"}), 500
#----------------------------------
@app.route("/api/streamer",methods=["GET"])#solo metodo get
def getStreamerByName():
    try:
        nameStreamer = request.args["name"]
        streamer = Streamers.query.filter_by(name=nameStreamer).first()
        if not streamer:
            return jsonify({"smg":"este streamer no existe"}), 200
        else:
            return jsonify(streamer.serialize()),200
    
    except Exception:
        exception("error")
        return jsonify({"smg":"ha ocurrido un error"}), 500
#----------------------------------
@app.route("/api/findstreamer",methods=["GET"])#solo metodo get
def getStreamer():
    try:

        fields={}
        if "name" in request.args:
            fields["name"] = request.args["name"]
        
        if "subs" in request.args:
            fields["subs"] = request.args["subs"]

        if "followers" in request.args:
            fields["followers"] = request.args["followers"]

        streamer = Streamers.query.filter_by(**fields).first()
        if not streamer:
            return jsonify({"smg":"este streamer no existe"}), 200
        else:
            return jsonify(streamer.serialize()),200
    
    except Exception:
        exception("error")
        return jsonify({"smg":"ha ocurrido un error"}), 500
#----------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=4000)
