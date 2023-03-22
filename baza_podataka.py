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
    godina_dve_cifre = db.Column(db.Integer, nullable=False, default=int(datetime.now().strftime('%y')))
    ime_izvrsioca = db.Column(db.String(250), nullable=False)
    ime_saradnika_1 = db.Column(db.String(250), nullable=False)
    datum_naloga = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datum_vreme_pocetka = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    datum_vreme_kraja = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    EE_objekat = db.Column(db.String(250), nullable=False)
    opis_zadatka = db.Column(db.String(500), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Nalozi {self.ime_izvrsioca}>'
    
    def pretrazi_db_po_datumu(self, vreme_pocetka, vreme_kraja, ime):
        return Nalozi.query.filter(Nalozi.datum_naloga > vreme_pocetka,
                                   Nalozi.datum_naloga < vreme_kraja, Nalozi.ime_izvrsioca == ime).all()

    def pretrazi_db_po_vrednosti(self, vrednost_za_pretragu):
        return Nalozi.query.filter_by(broj_naloga=vrednost_za_pretragu).first()

    def svi_nalozi_lista(self):
        return db.session.query(Nalozi).all()

    pass
    # Kreiranje tabele po klasi Nalozi


"""Prvo uvozimo db i Nalozi klase iz baza_podataka modula. 
Zatim koristimo db.session.query da bismo izvršili upit nad bazom podataka.
U ovom upitu koristimo funkciju db.func.max da bismo pronašli maksimalnu vrednost u koloni "id". 
Ova funkcija se naziva kao metoda query objekta sesije, a njen rezultat se dobija pozivom metode scalar.
KOd je max_id = db.session.query(db.func.max(Nalozi.id)).scalar()"""