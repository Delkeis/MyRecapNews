from recapnews_app.database import db
from datetime import datetime
from enum import Enum
import logging as lg

class   Games(db.Model):
    __tablename__ = "games"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    path_to_img = db.Column(db.String(200), nullable=True)
    release_date = db.Column(db.DateTime)
    
    def __init__(self, title, description, release_date, path_to_img="none"):
        self.title = title
        self.description = description
        self.path_to_img = path_to_img
        self.release_date = release_date

class   News(db.Model):
        __tablename__ = "news"
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        gameTitle = db.Column(db.String(200), nullable=False)
        description = db.Column(db.String(800), nullable=False)
        path_to_img = db.Column(db.String(200), nullable=True)
        release_date = db.Column(db.DateTime)

        def __init__(self, title, gameTitle, description, release_date, path_to_img="none"):
            self.title = title
            self.gameTitle = gameTitle
            self.description = description
            self.release_date = release_date
            self.path_to_img = path_to_img

class   Priv(Enum):
    USER = 0
    ADMIN = 1

class   UserDb(db.Model):
    __tablename__ = "userdb"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50) , nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    privileges = db.Column(db.Enum(Priv))

    def __init__(self, db_name, db_lastname, db_password, db_privileges):
        self.firstname = db_name
        self.lastname = db_lastname
        self.password = db_password
        self.privileges = db_privileges

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Games("Doom", "description one", datetime.today(),"/static/image/Doom.png"))
    db.session.add(Games("wow", "description two", datetime.today()))
    db.session.add(News("wow news title", "wow", "wow news", datetime.today(),"/static/image/Doom.png"))
    db.session.add(News("doom news title", "Doom", "doom news", datetime.today(),"/static/image/wow.png"))
    #db.session.add(UserDb("jacquie", "tuning", "azerty", Priv['USER']))
    #db.session.add(UserDb("john", "doe", "qwerty", Priv['ADMIN']))
    db.session.commit()
    lg.warning('Database initialized!')