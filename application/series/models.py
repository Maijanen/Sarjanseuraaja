from application import db


class Serie(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date_created = db.Column(
                            'luotu', db.DateTime,
                            default=db.func.current_timestamp())
    date_modified = db.Column(
                            'muokattu', db.DateTime,
                            default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

    name = db.Column('nimi', db.String(144), nullable=False, unique=True)
    year = db.Column('julkaisuvuosi', db.Integer)
    info = db.Column('kuvaus', db.String(450))
    link = db.Column('linkki', db.String(300))

    def __init__(self, name, year, info, link):
        self.name = name
        self.year = year
        self.info = info
        self.link = link
