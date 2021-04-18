import pdfkit
from banner import Banner
import time
from banner import Banner



Banner.inv4sion()


print("\033[32mIsso pode levar alguns segundos...\033[m")

with open("../view/pdf_gen.html", 'w') as arquivo:
    arquivo.write('<style>html{text-aling:center;}</style>')
    arquivo.write('<center><h1>Emails Achados</h1></center>')
    arquivo.write("<br><br>")
    with open("../archives/emails.txt", "r") as emails_file:

        for linha in emails_file:
            arquivo.write(f"<center><h3>{linha}</h3></center>")

pdfkit.from_url('../view/pdf_gen.html', 'emails.pdf')
print("\033[32mPDF Gerado\033[m")
time.sleep(4)
