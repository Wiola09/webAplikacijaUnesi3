import os
from datetime import date, timedelta

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_value")
TODAY = date.today()
TOMOROW = date.today() + timedelta(days = 1)
MESEC_RANIJE = date.today() - timedelta(days = 30)
SLUZBE = ["СТКС10","СТКС20", "СТКС30"]
STKS10 = [("miroslavzeljkovic@gmail.com", 'Небојша Драгутиновић'), ("miroslavzeljkovic@gmail.com", 'Немања Максић'), ("miroslav.zeljkovic@ems.rs", 'Маријана Дмитрић'),
          ("miroslavzeljkovic@gmail.com", 'Иван Ћирић'), ("miroslavzeljkovic@gmail.com", 'Иван Гаровић'),
          ("miroslavzeljkovic@gmail.com", 'Александра Стојановић'), ("", "")]
STKS20 = [("miroslav.zeljkovic@ems.rs","Избор ЕМС"), ("miroslavzeljkovic@gmail.com", "Избор GMAIL"), ("", "")]
STKS30 = [("miroslav.zeljkovic@ems.rs","Јелена Ђуричић"), ("miroslavzeljkovic@gmail.com", "Срђан Митровић"),
          ("miroslavzeljkovic@gmail.com", "Далиборка Никчевић"), ("miroslavzeljkovic@gmail.com", "бруно Гаротић"),
          ("miroslavzeljkovic@gmail.com", "Мирослав Симовић"), ("miroslavzeljkovic@gmail.com", "Властимир Стојановић"), ("", "")
          ]

IMENA_ZAPOSLENIHA = ['Немања Максић', 'Маријана Дмитрић', 'Иван Ћирић', 'Иван Гаровић', 'Александра Стојановић', ""]
OBJEKTI = ["DV ekipa Bajina Bašta",	"Kneza Miloša 11", "Odmaralište Relejna Stanica Kopaonik", "Pogon Beograd",
           "Pogon Beograd - Cibuk",	"Pogon Bor",	"Pogon Kruševac",	"Pooslovni objekat Beograd", "Poslovna zgarada Kneza Milosa 11",
           "Poslovna zgrada - pogon Valjevo",	"Poslovna zgrada Kneza Miloša",	"Poslovna zgrada Kraljice Natalije",
           "Poslovna zgrada Krusevac",	"Poslovna zgrada Novi Sad",	"Poslovna zgrada Valjevo",	"Poslovna zgrada Vojvode Stepe",
           "Poslovni objekat kraljice Natalije",	"Poslovni objekat Rovinjska",	"Poslovni objekat Vojvode Stepe", 	"PRP Bor 4",
           "PRP Čibuk 1",	"RDC Bor",	"RDC Kruševac",	"RP Drmno",	"RP Đerdap 1",	"RP Đerdap 2",	"RP Mladost",	"RP Pančevo 1",
           "TS Bajina Bašta", "TS Beograd 17",	"TS Beograd 20"	,"TS Beograd 3",	"TS Beograd 4" ,"TS Beograd 5",
           "TS Beograd 8",	"TS Bistrica",	"TS Bor 2",	"TS Čačak 3",	"TS Jagodina 4",	"TS Kragujevac 2",	"TS Kraljevo 3",	"TS Kruševac 1"	,
           "TS Leskovac 2",	"TS Niš 2",	"TS Novi Sad 3",	"TS Obrenovac 400 kV","TS Pančevo 2",	"TS Požega",	"TS Sbotica 3",
           "TS Smederevo 3",	"TS Sombor",	"TS Srbobran",	"TS Sremska Mitrovica",	"TS Subotica",	"TS Šabac 3",	"TS Valač",	"TS Valjevo 3 / RDC Valjevo",
           "TS Vranje 4",	"TS Zrenjanin 2",	"Upravna zgrada PP Beograd",	"Upravna zgrada PP Bor",	"Upravna zgrada PP Kruševac",	"Upravna zgrada PP Niš"	,
           "Upravna zgrada PP Novi Sad",	"Upravna zgrada PP Valjevo",	"Vila Jasmin",	"Vila Karadžić",	"Vila Tetreb"]
gmail = 'miroslavzeljkovic@gmail.com'
mail_primalac = 'miroslav.zeljkovic@ems.rs'
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "default_value")

