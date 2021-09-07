from datetime import datetime
from .database import db
from .models import Games, News, UserDb, Priv

class DatabaseAcces():
    def delete_Games_entry(d_id):
        Games.query.filter_by(id=d_id).delete()
        db.session.commit()

    def delete_news_by_id(id):
        News.query.filter_by(id=id).delete()
        db.session.commit()

    def add_Games_entry(a_title, desc):
        new = Games(a_title, desc, datetime.today())
        db.session.add(new)
        db.session.commit()
    
    def set_new_pic(s_id, pic_path):
        Games.query.get(s_id).path_to_img = pic_path
        db.session.commit()
        print(Games.query.get(s_id).path_to_img)

    def set_new_desc(s_id, s_desc):
        Games.query.get(s_id).description = s_desc
        db.session.commit()

    def set_new_title(s_id, s_title):
        Games.query.get(s_id).title = s_title
        db.session.commit()

    def set_new_news_title(n_id, n_title):
        News.query.get(n_id).title = n_title
        db.session.commit()

    def set_new_news_description(n_id, n_desc):
        News.query.get(n_id).description = n_desc
        db.session.commit()

    def add_new_news(title, gameTitle, desc):
        myget = Games.query.filter_by(title=gameTitle).first()
        new = News(title, gameTitle, desc, datetime.today(), myget.path_to_img)
        db.session.add(new)
        db.session.commit()
