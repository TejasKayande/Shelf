
import os
from flask import Flask, render_template, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join(app.root_path, 'assets'), filename)



@app.route("/ExploreShelfs")
def exploreshelfs():
    return render_template('exploreshelfs.html')

@app.route("/ExploreBoards")
def exploreboards():
    return render_template('exploreboards.html')

@app.route("/")
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
