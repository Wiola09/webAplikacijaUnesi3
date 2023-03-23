import os

from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from sqlalchemy.sql.expression import func

from forms import CreatePostForm, PregledajBazu, IzaberiSluzbu, PretraziPoBroju, StampajNalog

from baza_podataka import db, Nalozi
from konstante import APP_SECRET_KEY, IMENA_ZAPOSLENIHA, STKS20, SLUZBE, STKS10, STKS30

from manipulacija_exel import PromeniEksel

app = Flask(__name__)

# CONNECT TO DB, kreiranje DB sa nazivom novi-nalozi-collection.db', specifično za SQL lite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nalozi6-collection.db'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL1", "sqlite:///nalozi-collection.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)  ### Ovaj deo je bio dok je class Nalozi(db.Model): bila definisna u ovom fajlu
db.init_app(app)  # vidi komentar u baza_podataka


app.config['SECRET_KEY'] = APP_SECRET_KEY
Bootstrap(app)


# #Kreiranje dokumenta nalozi3-collection.db
with app.app_context():
    db.create_all()


@app.route('/pregled_baze', methods=["GET", "POST"])
def pretraga_baze_po_datumu():
    form = PregledajBazu()
    lizabrana_lista_zaposlenih = STKS10 + STKS20 + STKS30
    form.ime_izvrsioca.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]

    broj_naloga_forma = PretraziPoBroju()


    if form.submit.data and form.validate_on_submit():
        # Podaci iz HTML forme
        ime_izvrsioca = form.ime_izvrsioca.data,
        datum_vreme_pocetka = form.datum_vreme_pocetka.data,
        datum_vreme_kraja = form.datum_vreme_kraja.data,
        print(ime_izvrsioca, " test22")


        # POZIVANJE METODA ZA PRETRAGU DB PO DATUMU
        # po_datumu = Nalozi.query.filter(Nalozi.datum_naloga > datum_vreme_pocetka[0],
        #                                 Nalozi.datum_naloga < datum_vreme_kraja[0]).all()

        po_datumu = Nalozi.pretrazi_db_po_datumu(Nalozi, datum_vreme_pocetka[0], datum_vreme_kraja[0], ime_izvrsioca[0])
        duzina_liste = len(po_datumu)

        # Zastita za praznu listu
        if duzina_liste == 0:
            print("duzina 0")
            return render_template("prazna_lista_pretrage.html")

        return render_template("/pregled_baze_sadržaj.html", prenesiUHTML=po_datumu, duzina_liste=duzina_liste,
                               pocetak_intervala=datum_vreme_pocetka[0], kraj_intervala=datum_vreme_kraja[0])

    if broj_naloga_forma.submit2.data and broj_naloga_forma.validate_on_submit():
        broj_naloga_iz_forme = broj_naloga_forma.broj_naloga.data
        print(broj_naloga_iz_forme, "ovo")
        if broj_naloga_iz_forme:
            print("ono")

        return redirect(url_for("nalog_na_stampu", slanje_broja_naloga_u_nalog_na_stampu=broj_naloga_iz_forme))

    return render_template("/pregled_baze.html", prenesiUHTML=form, broj_naloga_forma=broj_naloga_forma)


@app.route("/biranje_sluzbe", methods=["GET", "POST"])
def biranje_sluzbe():
    form = IzaberiSluzbu()
    if form.validate_on_submit():
        ime_sluzbe = form.izaberi_sluzbu.data
        print(ime_sluzbe)

        return redirect(url_for("pocetna_kreiranje_naloga", spisak=ime_sluzbe))
    return render_template("biranje_sluzbe.html", prenesiUHTML=form)


@app.route("/", methods=["GET", "POST"])
def pocetna():


    # max_id = db.session.query(db.func.max(Nalozi.id)).scalar()
    # objekat = Nalozi.query.filter_by(id=max_id).first()
    #
    # print(max_id)
    # print(objekat.broj_naloga)
    #
    # from datetime import datetime
    #
    # trenutna_godina = int(datetime.now().strftime('%y'))
    # print(trenutna_godina)
    # print(type(int(trenutna_godina)))
    # print(trenutna_godina)

    return render_template("index.html")


@app.route("/posalji_pojedinacan_nalog", methods=["GET", "POST"])
def nalog_na_stampu():
    primljen_broj_naloga = request.args.get('slanje_broja_naloga_u_nalog_na_stampu')

    objekat_nalog = Nalozi.pretrazi_db_po_vrednosti(Nalozi, vrednost_za_pretragu=primljen_broj_naloga)

    """ Zastita u slučaju da je pojedinačan nalog ne postoji"""
    if str(type(objekat_nalog)) == "<class 'NoneType'>":
        return render_template("prazna_lista_pretrage.html")

    form = StampajNalog()
    if form.validate_on_submit():
        mail_za_slanje = [form.mail.data]
        print(mail_za_slanje, "Štampaj nalog")
        editovanje_eksel_naloga_objekat = PromeniEksel()
        broj_naloga = editovanje_eksel_naloga_objekat.posalji_postojeci(objekat_nalog,mail_za_slanje)
        stanje = "послат"

        return render_template("uspesno_kreiran_nalog.html", stanje=stanje)


    print(objekat_nalog)
    print(type(objekat_nalog))
    # print(objekat_nalog.ime_izvrsioca)
    print("vratio sa stranice prikazi nalog")
    print(objekat_nalog.broj_naloga)


    return render_template("prikazi_nalog.html", objekat_nalog=objekat_nalog, dugme_posalji=form)


@app.route("/kreiraj_nalog", methods=["GET", "POST"])
def pocetna_kreiranje_naloga():
    spisak = request.args.get('spisak')

    print(spisak)
    form = CreatePostForm()
    if spisak == SLUZBE[0]:
        lizabrana_lista_zaposlenih = STKS10
        form.ime_saradnika_1.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_saradnika_2.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_izvrsioca.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
    elif spisak == SLUZBE[1]:
        lizabrana_lista_zaposlenih = STKS20
        form.ime_saradnika_1.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_saradnika_2.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_izvrsioca.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
    elif spisak == SLUZBE[2]:
        lizabrana_lista_zaposlenih = STKS30
        form.ime_saradnika_1.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_saradnika_2.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
        form.ime_izvrsioca.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
    else:
        lizabrana_lista_zaposlenih = IMENA_ZAPOSLENIHA
    form.ime_saradnika_1.choices = [ime[1] for ime in lizabrana_lista_zaposlenih]
    if form.validate_on_submit():

        # Podaci iz HTML forme
        datum_naloga = form.datum_naloga.data,
        ime_izvrsioca = form.ime_izvrsioca.data,
        ime_saradnika_1 = form.ime_saradnika_1.data,

        ime_saradnika_2 = form.ime_saradnika_2.data,
        datum_vreme_pocetka = form.datum_vreme_pocetka.data,
        datum_vreme_kraja = form.datum_vreme_kraja.data,
        EE_objekat = form.EE_objekat.data,
        opis_zadatka = form.opis_zadatka.data,

        # Resavanje problema vracanja samo jedne vrednosti po polju iz forme, a istvremeno sam zeleo da zadržim slistu
        # STKS10         # U kodu iznad sam kreirao listu choices, na osnovnu liste tupla STKS10, gde sam iz
        # svakog tupla birao samo vrednost sa imenom kada mi forma vrati ime, uhvatim ga u selected_value_saradnik1,
        # ali onda pretražujem STKS10 po toj vrednost i next vraca prvi "mec", i dobijam tuple

        selected_value_saradnik1 = ime_saradnika_1[0]
        selected_tuple_saradnik1 = next((t for t in lizabrana_lista_zaposlenih if t[1] == selected_value_saradnik1), None)
        print(selected_tuple_saradnik1)
        selected_value_izvrsilac = ime_izvrsioca[0]
        selected_tuple_izvrsilac = next((t for t in lizabrana_lista_zaposlenih if t[1] == selected_value_izvrsilac), None)
        print(selected_tuple_izvrsilac)

        mail_za_slanje = [selected_tuple_saradnik1[0], 'miroslavzeljkovic@gmail.com']
        print(mail_za_slanje)

        # UPISIVANJE NALOGA U BAZU PODATAKA
        nalog = Nalozi(broj_naloga="102/23", ime_izvrsioca=ime_izvrsioca[0], ime_saradnika_1=ime_saradnika_1[0],
                       datum_naloga=datum_naloga[0], datum_vreme_pocetka=datum_vreme_pocetka[0],
                       datum_vreme_kraja=datum_vreme_kraja[0], EE_objekat=EE_objekat[0], opis_zadatka=opis_zadatka[0])

        # #KREIRANJE NALOGA
        editovanje_eksel_naloga_objekat = PromeniEksel()
        broj_naloga = editovanje_eksel_naloga_objekat.izmeni(nalog, mail_za_slanje)

        # broj_naloga = editovanje_eksel_naloga_objekat.izmeni(datum_naloga[0],ime_izvrsioca[0], ime_saradnika_1[0],
        #                                                      ime_saradnika_2[0], datum_vreme_pocetka[0],
        #                                                      datum_vreme_kraja[0], EE_objekat[0],opis_zadatka[0],
        #                                                      mail_za_slanje= mail_za_slanje)

        print(broj_naloga)
        nalog.broj_naloga = broj_naloga
        #  !!! Iz nekog razloga moram da snimmim u bazu posle KREIRANJE NALOGA
        db.session.add(nalog)
        db.session.commit()
        stanje = "креиран"

        return render_template("uspesno_kreiran_nalog.html", stanje=stanje)

    return render_template("Unos_podataka_u_nalog.html", prenesiUHTML=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


# Ovo mi može trebati jedino ako dodam hipervezu za pregled svih naloga
# @app.route("/pregled_baze_sadržaj.html")
# def get_all_posts2():
#     try:
#         svi_nalozi = db.session.query(Nalozi).all()
#     except:
#         pass
#
#     return render_template("/pregled_baze_sadržaj.html",prenesiUHTML=svi_nalozi)
