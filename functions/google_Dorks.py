from googlesearch import search
import sys
from time import sleep
import os 
from banner import Banner



Banner.inv4sion()
with open("../archives/site.txt", "w") as arquivo:
    arquivo.write("")

class Dorks:

    def __init__(self, dominio):
        self.dominio = dominio

    def google(self):
        for resultados in search(f"{self.dominio}", stop=10):
            print(f"{resultados}")
            with open("../archives/site.txt", "a") as arquivo:
                arquivo.write(f"{resultados}\n")
            sleep(1)
        
    def pastebin(self):
        for resultados in search(f"site:pastebin.com {self.dominio}", stop=10):
            print(f"{resultados}")
            with open("../archives/site.txt", "a") as arquivo:
                arquivo.write(f"{resultados}\n")
        for resultados in search(f"site:pastebin.com intext:'{self.dominio}'", stop=10):
            print(f"{resultados}")
            with open("../archives/site.txt", "a") as arquivo:
                arquivo.write(f"{resultados}\n")

    def github(self):
        for resultados in search(f"site:github.com '{self.dominio}'", stop=10):
            print(f"{resultados}")
            with open("../archives/site.txt", "a") as arquivo:
                arquivo.write(f"{resultados}\n")


if __name__ == "__main__":
    resposta = input("Domínio:")
    root = Dorks(resposta)
    root.google()
    root.pastebin()
    root.github()

