
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, \
    SelectMultipleField, HiddenField, EmailField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

from konstante import TODAY, TOMOROW, MESEC_RANIJE, SLUZBE, IMENA_ZAPOSLENIHA, OBJEKTI, STKS20


# #WTForm
class CreatePostForm(FlaskForm):
    datum_naloga = DateField('Датум налога', format='%Y-%m-%d', default=TODAY, validators=[DataRequired()])
    ime_izvrsioca = SelectField("Име извршиоца", choices=[], validators=[DataRequired()])
    ime_saradnika_1 = SelectField("Име сарадника 1", default="", choices=[])
    ime_saradnika_2 = SelectField("Име сарадника 2", default="", choices=[])
    datum_vreme_pocetka = DateField("Датум и време почетка", format='%Y-%m-%d', default=TOMOROW, validators=[DataRequired()])
    datum_vreme_kraja = DateField("Датум и време краја", format='%Y-%m-%d', default=TOMOROW, validators=[DataRequired()])

    EE_objekat = SelectField("ЕЕ објекат: ", choices=OBJEKTI)
    broj_naloga = HiddenField()

    opis_zadatka = CKEditorField("Опис задатка:", default="Интервенција на мултиплексној опреми", validators=[DataRequired()])
    submit = SubmitField("Креирај путни налог и пошаљи налог на маил")


class PregledajBazu(FlaskForm):
    # datum_naloga = DateField('Датум налога', format='%Y-%m-%d', default=today, validators=[DataRequired()])
    ime_izvrsioca = SelectField("Име сарадника 1", choices=[])

    datum_vreme_pocetka = DateField("Почетак временског интервала", format='%Y-%m-%d', default=MESEC_RANIJE, validators=[DataRequired()])
    datum_vreme_kraja = DateField("Крај временског интервала", format='%Y-%m-%d', default=TOMOROW, validators=[DataRequired()])
    submit = SubmitField("Претражи по извршоцу и датуму")


class IzaberiSluzbu(FlaskForm):
    izaberi_sluzbu = SelectField("Одабери службу из падајуће листе ", default="", choices=SLUZBE)
    # izaberi_sluzbu2 =SelectMultipleField('Ime saradnika', choices=[
    #     ('1', 'Ime saradnika 1'),
    #     ('2', 'Ime saradnika 2'),
    #     ('3', 'Ime saradnika 3')
    # ])
    submit = SubmitField("Изабери службу")


class PretraziPoBroju(FlaskForm):
    broj_naloga = StringField("Унеси Број налога", default="2", validators=[DataRequired()])

    submit2 = SubmitField("Прикажи налог")


class StampajNalog(FlaskForm):
    # broj_naloga = HiddenField()
    mail = EmailField("Унеси маил", default="miroslavzeljkovic@gmail.com")

    submit2 = SubmitField("Пошаљи налог на маил")


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

