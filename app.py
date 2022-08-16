from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Baba##thunday@localhost:5432/progress'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  
def __init__(self, id, name):
      self.id = id
      self.name = name

db.create_all()
@app.route('/')

@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    name = request.form["name"]
    id = request.form["id"]
    entry = Person(name, id)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

