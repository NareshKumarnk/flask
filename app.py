from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://naresh:password@postgresql-im0i/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, id, pname, color):
        self.id = id
        self.pname = pname
        self.color = color

@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    id = request.form["id"]
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(id, pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()
