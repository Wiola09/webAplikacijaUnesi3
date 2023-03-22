import openpyxl
import os
import sys
from slanje_exel import PosaljiMail
from baza_podataka import db, Nalozi
from datetime import datetime


# Asks the user to enter the filepath of the excel file.
# filePath = input('Please enter the path of the folder where the excel files are stored: ')
# print(filePath)

# KORISTENJE APSOLUTNE PUTANJE
filePath = r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Orginal"
filePath2 = r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Napravljeni nalozi"

# KORISTENJE RELATIVNE PUTANJE
# Goes inside that folder.
filePath3 = r"static/db/osnovni"
filePath4 = r"static/db"
abs_path = os.path.join(os.getcwd(), filePath3)
abs_path_nalozi = os.path.join(os.getcwd(), filePath4)

print(abs_path)
print(filePath3, "ovaj")

# PROMENA RADNOG DIREKTORIJUMA
os.chdir(abs_path)

print(os.getcwd())
dirname = os.path.dirname(__file__)
print(dirname)
print(os.getcwd())

# Gets the list of excel files inside the folder.
excelFiles = os.listdir('.')
print(excelFiles)

# Ovim kodom sam uspeo da na exel dokumentu, izaberem prvu stranicu, i da onda na njoj menjam vrednosti
# Samo mi se jedan fajl nalazi na putanji, pa biram njega
try:
    wb = openpyxl.load_workbook(excelFiles[0])
except:
    wb = openpyxl.load_workbook(excelFiles[1])

print(os.getcwd())


class PromeniEksel:
    def __init__(self):
        print("PromeniEksel")

    # def izmeni(self,datum_naloga,ime_izvrsioca, ime_saradnika_1, ime_saradnika_2,
    #            datum_vreme_pocetka,datum_vreme_kraja, EE_objekat, opis_zadatka, mail_za_slanje):
    def posalji_postojeci(self, nalog,mail_za_slanje):
        wb['Novi RZ']['C4'].value = nalog.datum_naloga
        # Извршилац
        wb['Novi RZ']['D13'].value = nalog.ime_izvrsioca
        # Сарадник
        wb['Novi RZ']['C16'].value = nalog.ime_saradnika_1
        # Време почетка и краја
        wb['Novi RZ']['C27'].value = nalog.datum_vreme_pocetka
        wb['Novi RZ']['F27'].value = nalog.datum_vreme_kraja
        #    у ЕЕ објекту на делу објекта - ТК  система:
        wb['Novi RZ']['E25'].value = nalog.EE_objekat
        # Опис задатка:
        wb['Novi RZ']['A31'].value = nalog.opis_zadatka

        wb['Novi RZ']['G7'].value = f"{nalog.broj_naloga}/23"

        naziv_dokumenta = f"Nalog Broj postojeci broj {nalog.broj_naloga}_23.xlsx"
        #  odlazak na objekat {EE_objekat} problem sa enkodingom kod slanja fajla u mailu

        os.chdir(abs_path_nalozi)
        wb.save(naziv_dokumenta)
        print("kreiran dokument")
        print(mail_za_slanje, "mail iz pretraga naloga")

        objekat_mail = PosaljiMail()
        objekat_mail.posalji_mail(naziv_dokumenta, nalog.ime_izvrsioca, nalog.datum_naloga, nalog.EE_objekat,
                                  nalog.broj_naloga, mail_za_slanje)

    def izmeni(self, nalog, mail_za_slanje):

        print(nalog.datum_naloga)

        def promeni_exel_osim_broja_naloga():
            # Deo koda zaduzen za promene vrednosti polja u exel dokumentu
            # Датум

            wb['Novi RZ']['C4'].value = nalog.datum_naloga
            # Извршилац
            wb['Novi RZ']['D13'].value = nalog.ime_izvrsioca
            # Сарадник
            wb['Novi RZ']['C16'].value = nalog.ime_saradnika_1
            # Време почетка и краја
            wb['Novi RZ']['C27'].value = nalog.datum_vreme_pocetka
            wb['Novi RZ']['F27'].value = nalog.datum_vreme_kraja
            #    у ЕЕ објекту на делу објекта - ТК  система:
            wb['Novi RZ']['E25'].value = nalog.EE_objekat
            # Опис задатка:
            wb['Novi RZ']['A31'].value = nalog.opis_zadatka
            joj = "/".join((str(spojen_broj_naloga), "23"))
            wb['Novi RZ']['G7'].value = joj



            # print(wb['Novi RZ']['A31'].value)
            # ##############################################################################3
        # datum_naloga=datum_naloga
        # ime_izvrsioca = form.ime_izvrsioca.data,
        # ime_saradnika_1 = form.ime_saradnika_1.data,
        # ime_saradnika_2 = form.ime_saradnika_2.data,
        #
        # datum_vreme_pocetka = form.datum_vreme_pocetka.data,
        # datum_vreme_kraja = form.datum_vreme_kraja.data,
        # EE_objekat = form.EE_objekat.data,
        # opis_zadatka = form.opis_zadatka.data,

        """Deo koda u kom sam ranije uzimao poslednji broj naloga iz exel dokumenta
        # ### Deo koda zaduzen za otvaranje templejta naloga, uzimanje broja naloga,
        # uvecavanje za jedan i snimanje u templejt, snimam da bih sacuvao redosled brojeva naloga
        # Obratiti paznju jer odakle treba da uzima broj naloga """

        # trenutna_vrenost_broja_naloga = wb['Novi RZ']['G7'].value
        # lista_broj_naloga = trenutna_vrenost_broja_naloga.split("/")
        #
        # trenutna_vrenost_broja_naloga = lista_broj_naloga[0]
        # trenutna_vrenost_broja_naloga = int(trenutna_vrenost_broja_naloga)
        # novi_broj = trenutna_vrenost_broja_naloga + 1
        # spojen_broj_naloga = "/".join((str(novi_broj), lista_broj_naloga[1]))
        # wb['Novi RZ']['G7'].value = spojen_broj_naloga
        # try:
        #     wb.save(excelFiles[0])
        # except:
        #     wb.save(excelFiles[1])
        def promeni_format_broja_naloga(broj):
            lista_broj_naloga = broj.split("_")
            trenutna_vrenost_broja_naloga = lista_broj_naloga[0]
            trenutna_vrenost_broja_naloga = int(trenutna_vrenost_broja_naloga)
            novi_broj = trenutna_vrenost_broja_naloga + 1
            spojen_broj_naloga_kosa_crta = "/".join((str(novi_broj), lista_broj_naloga[1]))
            print(spojen_broj_naloga_kosa_crta)
            return spojen_broj_naloga_kosa_crta

        max_id = db.session.query(db.func.max(Nalozi.id)).scalar()
        objekat = Nalozi.query.filter_by(id=max_id).first()

        print(max_id)
        try:
            print(objekat.broj_naloga)
            type(objekat.broj_naloga)
            spojen_broj_naloga = objekat.broj_naloga
            type(spojen_broj_naloga)
        except:
            spojen_broj_naloga = 0
        print(type(spojen_broj_naloga))
        spojen_broj_naloga = int(spojen_broj_naloga) + 1

        # #####################################################################################

        promeni_exel_osim_broja_naloga()
        # #####################################################################################

        # ## Ovaj kod je zaduzen za snimanje naloga , pri cemu ej deo koda zadužen za konvertovanje 23/23 u 23_23

        # spojen_broj_naloga = spojen_broj_naloga.replace("/", "_")

        broj_test = f"{str(spojen_broj_naloga)}_{(datetime.now().strftime('%y'))}"

        naziv_dokumenta = f"Nalog Broj {broj_test} za {nalog.ime_izvrsioca} dana {nalog.datum_naloga} " \
                          f"odlazak na objekat {nalog.EE_objekat}.xlsx"
        #  odlazak na objekat {EE_objekat} problem sa enkodingom kod slanja fajla u mailu

        os.chdir(abs_path_nalozi)
        wb.save(naziv_dokumenta)
        lista_fajlova = os.listdir('.')
        print(lista_fajlova)
        print(excelFiles[0] + ' completed.')

        # ## Kreiranje objekta posalji mail i slanje maila
        objekat_mail = PosaljiMail()
        objekat_mail.posalji_mail(naziv_dokumenta, nalog.ime_izvrsioca, nalog.datum_naloga, nalog.EE_objekat,
                                  broj_test, mail_za_slanje)

        # filePath = r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Orginal"
        # os.chdir(filePath)
        return spojen_broj_naloga
        # sys.exit()


