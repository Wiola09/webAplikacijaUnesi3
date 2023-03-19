import openpyxl
import os
import sys
from slanje_exel import PosaljiMail

# Asks the user to enter the filepath of the excel file.
# filePath = input('Please enter the path of the folder where the excel files are stored: ')
# print(filePath)

# KORISTENJE APSOLUTNE PUTANJE
filePath = r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Orginal"
filePath2 =r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Napravljeni nalozi"

#KORISTENJE RELATIVNE PUTANJE
# Goes inside that folder.
filePath3 = r".\static\db\osnovni"
print(filePath3, "ovaj")

### PROMENA RADNOG DIREKTORIJUMA
os.chdir(filePath3)

print(os.getcwd())
dirname = os.path.dirname(__file__)
print(dirname)
print(os.getcwd())

# Gets the list of excel files inside the folder.
excelFiles = os.listdir('.')
print(excelFiles)


# Samo mi se jedan fajl nalazi na putanji, pa biram njega
wb = openpyxl.load_workbook(excelFiles[1])

print(os.getcwd())


class PromeniEksel():
    def __init__(self):
        print("PromeniEksel")

    def izmeni(self,datum_naloga,ime_izvrsioca, ime_saradnika_1, ime_saradnika_2,
               datum_vreme_pocetka,datum_vreme_kraja, EE_objekat,opis_zadatka):

        # datum_naloga=datum_naloga
        # ime_izvrsioca = form.ime_izvrsioca.data,
        # ime_saradnika_1 = form.ime_saradnika_1.data,
        # ime_saradnika_2 = form.ime_saradnika_2.data,
        #
        # datum_vreme_pocetka = form.datum_vreme_pocetka.data,
        # datum_vreme_kraja = form.datum_vreme_kraja.data,
        # EE_objekat = form.EE_objekat.data,
        # opis_zadatka = form.opis_zadatka.data,
        #Ovim kodom sam uspeo da na exel dokumentu, izaberem prvu stranicu, i da onda na njoj menjam vrednosti

        trenutna_vrenost_broja_naloga = wb['Novi RZ']['G7'].value
        lista_broj_naloga = trenutna_vrenost_broja_naloga.split("/")

        trenutna_vrenost_broja_naloga = lista_broj_naloga[0]
        trenutna_vrenost_broja_naloga = int(trenutna_vrenost_broja_naloga)
        novi_broj = trenutna_vrenost_broja_naloga + 1
        spojen_broj_naloga = ("/").join((str(novi_broj), lista_broj_naloga[1]))
        wb['Novi RZ']['G7'].value = spojen_broj_naloga

        wb.save(excelFiles[1])
        # Датум
        wb['Novi RZ']['C4'].value = datum_naloga

        # Извршилац
        wb['Novi RZ']['D13'].value = ime_izvrsioca

        #Сарадник
        wb['Novi RZ']['C16'].value = ime_saradnika_1

        #Време почетка и краја
        wb['Novi RZ']['C27'].value= datum_vreme_pocetka
        wb['Novi RZ']['F27'].value= datum_vreme_kraja

        #    у ЕЕ објекту на делу објекта - ТК  система:
        wb['Novi RZ']['E25'].value = EE_objekat

        #Опис задатка:
        wb['Novi RZ']['A31'].value = opis_zadatka

        # print(wb['Novi RZ']['A31'].value)

        ### Uzimanje broja naloga i pisanje novog za jedan uvecanog
        # Obratiti paznju jer odakle treba da uzima broj naloga
        spojen_broj_naloga
        spojen_broj_naloga = spojen_broj_naloga.replace("/", "_")

        naziv_dokumenta = f"Nalog Broj {spojen_broj_naloga} za {ime_izvrsioca} dana {datum_naloga} odlazak na objekat {EE_objekat}.xlsx"   #  odlazak na objekat {EE_objekat} problem sa enkodingom kod slanja fajla u mailu
        os.chdir(filePath2)
        wb.save(naziv_dokumenta)
        print(excelFiles[1] + ' completed.')
        objekat_mail=PosaljiMail()
        objekat_mail.posalji_mail(naziv_dokumenta, ime_izvrsioca, datum_naloga, EE_objekat, spojen_broj_naloga)
        filePath = r"C:\Users\Miroslav\OpenAI\EXEL 2 open\Orginal"
        os.chdir(filePath)
        return spojen_broj_naloga
        # sys.exit()

