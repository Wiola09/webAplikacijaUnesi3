
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateTimeField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from datetime import datetime, date, timedelta

today = date.today()
tomorow = date.today() + timedelta(days = 1)
mesec_ranije = date.today() - timedelta(days = 30)
IMENA_ZAPOSLENIH = ['Немања Максић', 'Маријана Дмитрић', 'Иван Ћирић', 'Иван Гаровић', 'Александра Стојановић', ""]
OBJEKTI = ["DV ekipa Bajina Bašta",	"Kneza Miloša 11", "Odmaralište Relejna Stanica Kopaonik", "Pogon Beograd",
           "Pogon Beograd - Cibuk",	"Pogon Bor",	"Pogon Kruševac",	"Pooslovni objekat Beograd", "Poslovna zgarada Kneza Milosa 11",
           "Poslovna zgrada - pogon Valjevo",	"Poslovna zgrada Kneza Miloša",	"Poslovna zgrada Kraljice Natalije",
           "Poslovna zgrada Krusevac",	"Poslovna zgrada Novi Sad",	"Poslovna zgrada Valjevo",	"Poslovna zgrada Vojvode Stepe",
           "Poslovni objekat kraljice Natalije",	"Poslovni objekat Rovinjska",	"Poslovni objekat Vojvode Stepe", 	"PRP Bor 4",
           "PRP Čibuk 1",	"RDC Bor",	"RDC Kruševac",	"RP Drmno",	"RP Đerdap 1",	"RP Đerdap 2",	"RP Mladost",	"RP Pančevo 1",
           "TS Bajina Bašta"	,"TS Beograd 17",	"TS Beograd 20"	,"TS Beograd 3",	"TS Beograd 4" ,"TS Beograd 5",
           "TS Beograd 8",	"TS Bistrica",	"TS Bor 2",	"TS Čačak 3",	"TS Jagodina 4",	"TS Kragujevac 2",	"TS Kraljevo 3",	"TS Kruševac 1"	,
           "TS Leskovac 2",	"TS Niš 2",	"TS Novi Sad 3",	"TS Obrenovac 400 kV","TS Pančevo 2",	"TS Požega",	"TS Sbotica 3",
           "TS Smederevo 3",	"TS Sombor",	"TS Srbobran",	"TS Sremska Mitrovica",	"TS Subotica",	"TS Šabac 3",	"TS Valač",	"TS Valjevo 3 / RDC Valjevo",
           "TS Vranje 4",	"TS Zrenjanin 2",	"Upravna zgrada PP Beograd",	"Upravna zgrada PP Bor",	"Upravna zgrada PP Kruševac",	"Upravna zgrada PP Niš"	,
           "Upravna zgrada PP Novi Sad",	"Upravna zgrada PP Valjevo",	"Vila Jasmin",	"Vila Karadžić",	"Vila Tetreb"]

##WTForm
class CreatePostForm(FlaskForm):
    # datum_naloga = StringField("Датум налога", validators=[DataRequired()])
    datum_naloga = DateField('Датум налога', format='%Y-%m-%d', default=today, validators=[DataRequired()])
    ime_izvrsioca = StringField("Име извршиоца", default="Небојша Драгутиновић", validators=[DataRequired()])
    ime_saradnika_1 = SelectField("Име сарадника 1", choices= IMENA_ZAPOSLENIH)
    ime_saradnika_2 = SelectField("Име сарадника 2", default="", choices=IMENA_ZAPOSLENIH)
    datum_vreme_pocetka = DateField("Датум и време почетка", format='%Y-%m-%d', default=tomorow, validators=[DataRequired()])
    datum_vreme_kraja = DateField("Датум и време краја", format='%Y-%m-%d', default=tomorow, validators=[DataRequired()])

    EE_objekat = SelectField("ЕЕ објекат: ", choices=OBJEKTI)
    broj_naloga = HiddenField()

    opis_zadatka = CKEditorField("Опис задатка:", default="Интервенција на мултиплексној опреми", validators=[DataRequired()])
    submit = SubmitField("Креирај путни налог")

class PregledajBazu(FlaskForm):
    # datum_naloga = DateField('Датум налога', format='%Y-%m-%d', default=today, validators=[DataRequired()])
    ime_izvrsioca = StringField("Име извршиоца", default="Небојша Драгутиновић", validators=[DataRequired()])

    datum_vreme_pocetka = DateField("Почетак временског интервала", format='%Y-%m-%d', default=mesec_ranije, validators=[DataRequired()])
    datum_vreme_kraja = DateField("Крај временског интервала", format='%Y-%m-%d', default=tomorow, validators=[DataRequired()])
    submit = SubmitField("Претражи по извршоцу и датуму")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let me in!")

class CommentForm(FlaskForm):
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


