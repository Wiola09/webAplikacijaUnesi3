"""
https://stackoverflow.com/questions/14789668/separate-sqlalchemy-models-by-file-in-flask
@johnny It means that SQLAlchemy() does not have to take app as parameter in the module it is used. 
In most examples you can see SQLAlchemy(app) but it requires app from other scope in this case. 
Instead you can use uninitialized SQLAlchemy() and use init_app(app) method later 
as described in http://stackoverflow.com/a/9695045/2040487. –
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Nalozi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    broj_naloga = db.Column(db.String(250), nullable=False)
    ime_izvrsioca = db.Column(db.String(250), nullable=False)
    ime_saradnika_1 = db.Column(db.String(250), nullable=False)
    datum_naloga = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    EE_objekat = db.Column(db.String(250), nullable=False)
    opis_zadatka = db.Column(db.String(500), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Nalozi {self.ime_izvrsioca}>'
    
    def pretrazi_po_datumu(self, vreme_pocetka, vreme_kraja):
        return Nalozi.query.filter(Nalozi.datum_naloga > vreme_pocetka,
                            Nalozi.datum_naloga < vreme_kraja).all()

    pass
    # Kreiranje tabele po klasi Nalozi