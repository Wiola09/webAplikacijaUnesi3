import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import os

from konstante import gmail, mail_primalac, MAIL_PASSWORD

smtp_server = 'smtp.gmail.com'
smtp_port = 587
# Replace with your own gmail account
# mail_primalac = 'jelena.djuricic@ems.rs'
# mail_primalac = 'nebojsa.dragutinovic@ems.rs'

class PosaljiMail():
    def __init__(self):
        print("PosaljiMail")

    def posalji_mail(self, naziv_dokumenta,ime_izvrsioca, datum_naloga, EE_objekat, spojen_broj_naloga, mail_za_slanje ):
        message = MIMEMultipart('mixed')
        message['From'] = 'Putni nalozi STKS <{sender}>'.format(sender="test")
        # message['From'] = f'Radoslav Paunović <test@gmail.com>'
        message['To'] = "Zarko Veličković@ems.rs"
        message['CC'] = 'Kum.Raša@ems.rs'
        message['Subject'] = naziv_dokumenta

        msg_content = f'<h4>Поштовани,<br> У систему је за Вас креиран путни налог број {spojen_broj_naloga} за службени пут планиран дана {datum_naloga} на објекат {EE_objekat}.' \
					  f'<br> </h4>\n'

		# < a
		# href = "http://127.0.0.1:8080/" > Link < / >
        body = MIMEText(msg_content, 'html')
        message.attach(body)

        attachmentPath = f"c:\\Users\\Miroslav\\OpenAI\\EXEL 2 open\\Napravljeni nalozi\\{naziv_dokumenta}"
        attachmentPath = f"/opt/render/project/src/static/db/{naziv_dokumenta}"

        # varijanta za slanje sa racunara
        putanja_radna = os.getcwd()
        print(putanja_radna , "test_putanje")
        attachmentPath = f"{putanja_radna}/{naziv_dokumenta}"
        # [Errno 2] No such file or directory: '/opt/render/project/src/static/db/Nalog Broj 85_23 za Miroslav Zeljković dana 2023-03-20 odlazak na objekat DV ekipa Bajina Bašta.xlsx'

        print(os.getcwd(), "test_putanje")
        try:
            with open(attachmentPath, "rb") as attachment:

                # p = MIMEApplication(attachment.read(), _subtype="xlsx")   # !!! Imao sam problem sa enkodingom naziva
                # fajla, jedva resih sa basename(attachmentPath)

                p = MIMEApplication(
                    attachment.read(),
                    Name=basename(attachmentPath)
                )

                p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1])

                message.attach(p)



        except Exception as e:
            print(str(e))

        msg_full = message.as_string()

        context = ssl.create_default_context()

        #  za slanje na vise mail adresa smtplib prihvata listu !!!!
        # mail_primalac = [miroslav.zeljkovic@ems.rs, 'miroslavzeljkovic@gmail.com']
        mail_primalac = mail_za_slanje
        print(mail_primalac, "листа")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(gmail, MAIL_PASSWORD)

            server.sendmail(gmail, mail_primalac, msg_full)
            server.quit()

        print("email sent out successfully")
