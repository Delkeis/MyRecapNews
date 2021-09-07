import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory

app = Flask(__name__)
app.config.from_object("config")

from .models import Games, News, UserDb, Priv
from .database import db
from .manageDatabase import DatabaseAcces

@app.route('/favicon.ico')
def favicon():
    #fonction pour retouner l'icon d'onglet et favori
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

#uploader de fichier (sert à envoyer de images dans le dossier du serveur écrit aussi dans la db)
@app.route('/uploader/', methods=['GET', 'POST'])
def uploader():
    if  request.method == 'POST':
        my_file = request.files['picture']
        if my_file.filename != '':
            #enregistrer l'image sur le serveur
            my_file.save(os.path.join(app.config['UPLOAD_FOLDER'], my_file.filename))
            #on la lie dans la database
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], my_file.filename)):
                DatabaseAcces.set_new_pic(request.form['Id'], app.config['PIC_FOLDER']+my_file.filename)
    return redirect(url_for("gamesadmin"))
        
#page avec tout les jeux
@app.route('/games/', methods=['GET', 'POST'])
def games():
    content_req = Games.query.all()
    return render_template("games.html", list=content_req)

#page jeu unique (grande fiche)
@app.route('/game/fiche/', methods=['GET', 'POST'])
def game_page():
    #on prend l'id de la news en le contenu pour la distribuer au html
    p_id = request.args.get('id')
    #on récupère le contenue de la db pour le passer au html en argument
    a = Games.query.get(p_id)
    gameNews = News.query.filter_by(gameTitle=a.title)
    return  render_template("GameTemplate.html", pass_id=p_id, game=a, gamenews=gameNews)


#page d'administration/modification des jeux unique (grand format)
@app.route('/game/fiche/admin/', methods=['GET', 'POST'])
def game_admin():
    #on prend l'id de la news en le contenu pour la distribuer au html
    p_id = request.args.get('id')
    #on récupère le contenue de la db pour le passer au html en argument
    a = Games.query.get(p_id)
    gameNews = News.query.filter_by(gameTitle=a.title)
    #on vérifie le type de requète
    if request.method == 'POST':
        #on récupère le contenue du forms pour écrire sur la db
        if request.form['type'] == 'description':
            DatabaseAcces.set_new_desc(request.form['Id'], request.form['Desc'])
        elif request.form['type'] == 'title':
            DatabaseAcces.set_new_title(request.form['Id'], request.form['Title'])
        elif request.form['type'] == 'addnewnews':
            DatabaseAcces.add_new_news(request.form['Title'], a.title, request.form['Description'])
        elif request.form['type'] == 'modifinews':
            return redirect(url_for('news_fiche_admin', id=request.form['Id']))
        elif request.form['type'] == 'delnews':
            DatabaseAcces.delete_news_by_id(request.form['Id'])
    return render_template("gameadmin.html", game=a, isadmin=0, gamenews=gameNews)

#pour l'administration de la page jeux /Games
@app.route('/gamesadmin/', methods=['GET', 'POST'])
def gamesadmin():
    content_req = Games.query.all()
    #on filtre les requête POST et GET
    if request.method == 'POST':
    #on vérifie la nature de la requête
        if request.form['Button'] == 'delete':
            #on vas chercher dans la classe DatabaseAcces les methods qui me permettes de modifier la bd
            DatabaseAcces.delete_Games_entry(request.form['Id'])
            content_req = Games.query.all()
        elif request.form['Button'] == 'submit':
            DatabaseAcces.add_Games_entry(request.form['Title'], request.form['Description'])
            content_req = Games.query.all()
    return render_template("gamesadmin.html", list=content_req, isadmin=1)

#page home/news qui contient toutes les news de tout les jeux
@app.route('/')
@app.route('/news/')
def news():
    myNews = News.query.all()
    return render_template("news.html", content=myNews)

@app.route('/news/fiche/', methods=['GET', 'POST'])
def news_fiche():
    p_id = request.args.get('id')
    n = News.query.get(p_id)
    return render_template("newspage.html", passnews=n)

@app.route('/news/fiche/admin/', methods=['GET', 'POST'])
def news_fiche_admin(id=None):
    if id == None:
        id = request.args.get('id')
    n = News.query.get(id)
    print(n.gameTitle)
    if request.method == 'POST':
        if request.form['type'] == 'title':
            DatabaseAcces.set_new_news_title(request.form['Id'], request.form['Title'])
        elif request.form['type'] == 'description':
            DatabaseAcces.set_new_news_description(request.form['Id'], request.form['Desc'])
    return render_template("newspageadmin.html", passnews=n)

#page user (indisponible pour le moment)
@app.route('/user/', methods=['GET', 'POST'])
def user():
    return (render_template("user.html"))

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")
    
@app.route('/homeadmin/', methods=['GET', 'POST'])
def homeadmin():
    return render_template("homeadmin.html")

@app.route('/useradmin/', methods=['GET', 'POST'])
def useradmin():
    return render_template("useradmin.html")

if __name__ == "__main__":
    app.run()