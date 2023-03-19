import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap

from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, PregledajBazu

from baza_podataka import db, Nalozi


APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_value")

from manipulacija_exel import PromeniEksel
app = Flask(__name__)

##CONNECT TO DB, kreiranje DB sa nazivom novi-nalozi-collection.db', specifično za SQL lite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nalozi2-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)  ### Ovaj deo je bio dok je class Nalozi(db.Model): bila definisna u ovom fajlu
db.init_app(app)  # vidi komentar u baza_podataka


app.config['SECRET_KEY'] = APP_SECRET_KEY
Bootstrap(app)


##Kreiranje dokumenta nalozi3-collection.db
with app.app_context():
    db.create_all()


@app.route('//pregled_baze', methods=["GET", "POST"])
def pretraga_baze_po_datumu():
    form = PregledajBazu();
    if form.validate_on_submit():
        # Podaci iz HTML forme
        ime_izvrsioca=form.ime_izvrsioca.data,
        datum_vreme_pocetka = form.datum_vreme_pocetka.data,
        datum_vreme_kraja = form.datum_vreme_kraja.data,
        svi_nalozi = db.session.query(Nalozi).all()

        # POZIVANJE METODA ZA PRETRAGU DB PO DATUMU
        # po_datumu = Nalozi.query.filter(Nalozi.datum_naloga > datum_vreme_pocetka[0],Nalozi.datum_naloga < datum_vreme_kraja[0]).all()
        po_datumu = Nalozi.pretrazi_po_datumu(Nalozi, datum_vreme_pocetka[0], datum_vreme_kraja[0])
        duzina_liste=len(po_datumu)

        # Zastita za praznu listu
        if duzina_liste == 0:
            return render_template("test.html", prenesiUHTML=form)

        return render_template("/pregled_baze_sadržaj.html", prenesiUHTML=po_datumu, duzina_liste=duzina_liste, pocetak_intervala=datum_vreme_pocetka[0], kraj_intervala=datum_vreme_kraja[0])

    return render_template("/pregled_baze.html", prenesiUHTML=form)

# Ovo mi može trebati jedino ako dodam hipervezu za pregled svih naloga

# @app.route("/pregled_baze_sadržaj.html")
# def get_all_posts2():
#     try:
#         svi_nalozi = db.session.query(Nalozi).all()
#     except:
#         pass
#
#     return render_template("/pregled_baze_sadržaj.html",prenesiUHTML=svi_nalozi)

@app.route("/", methods=["GET", "POST"])
def pocetna_kreiranje_naloga():
    form = CreatePostForm();
    if form.validate_on_submit():

        # Podaci iz HTML forme
        datum_naloga=form.datum_naloga.data,
        ime_izvrsioca=form.ime_izvrsioca.data,
        ime_saradnika_1 = form.ime_saradnika_1.data,
        ime_saradnika_2 = form.ime_saradnika_2.data,
        datum_vreme_pocetka= form.datum_vreme_pocetka.data,
        datum_vreme_kraja = form.datum_vreme_kraja.data,
        EE_objekat = form.EE_objekat.data,
        opis_zadatka = form.opis_zadatka.data,

        #KREIRANJ NALOGA
        editovanje_eksel_naloga_objekat = PromeniEksel()
        broj_naloga = editovanje_eksel_naloga_objekat.izmeni(datum_naloga[0],ime_izvrsioca[0], ime_saradnika_1[0], ime_saradnika_2[0],
               datum_vreme_pocetka[0],datum_vreme_kraja[0], EE_objekat[0],opis_zadatka[0])

        # UPISIVANJE NALOGA U BAZU PODATAKA
        nalog = Nalozi(broj_naloga=broj_naloga, ime_izvrsioca=ime_izvrsioca[0], ime_saradnika_1=ime_saradnika_1[0],
                       datum_naloga=datum_naloga[0], EE_objekat=EE_objekat[0], opis_zadatka=opis_zadatka[0])
        db.session.add(nalog)
        db.session.commit()

        return render_template("uspesno_kreiran_nalog.html")

    return render_template("test.html", prenesiUHTML=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
