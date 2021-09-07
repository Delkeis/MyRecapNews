import os
from flask import Flask

from .views import app
from recapnews_app import database
from .models import Games

database.db.init_app(app)

@app.cli.command("init_db")
def init_db():
    models.init_db()
