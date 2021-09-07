import os

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DELK_APP_ID = 1200420960103822

#initialise la base de donnée de l'application
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#upload des fichiers
UPLOAD_FOLDER = '/var/www/recapnews/recapnews_app/static/image/'
#UPLOAD_FOLDER = '/home/Delkeis/repo/recapnews/recapnews_app/static/image/'

PIC_FOLDER = '/image/'
ALLOWED_EXTENTION = {'png', 'jpg', 'jpeg'}