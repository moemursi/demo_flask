from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False ,unique=True)

    def __repr__(self):
        return f'<Person {self.id} , {self.name}>'

user1 = Person(name='adam')
user2 = Person(name='robyn')
user3 = Person(name='aaron')

db.session.add_all([user1,user2,user3])
db.session.commit()
db.create_all()


@app.route('/')
def index():
    name = Person.query.first()
    return f"Hello, World {name.name} "