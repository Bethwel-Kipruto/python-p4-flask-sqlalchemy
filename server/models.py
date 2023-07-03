from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Owner(db.Model):
    __tablename__ ='owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String)
    
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'

class Pets(db.Model):
    __tablename__ ='pets'

    id = db.Column(db.Integer, primary_key=True)
    species = db.column(db.String)
    owner = db.column(db.String, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'    