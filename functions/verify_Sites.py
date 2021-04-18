import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
from selenium import webdriver
from email.utils import parseaddr
from selenium.webdriver.firefox.options import Options
import re
import os

class CrawlerSites:
    def __init__(self, sites):
        self.sites = sites

    def pastebin(self):
        try:
            with open("../archives/html_content.txt", "a") as arquivo:
                arquivo.write(f'{requests.get(self.sites).text}\n')

            with open("../archives/html_content.txt", "r") as arquivo:
                for line in arquivo:
                    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

                    cleantext = re.sub(cleanr, '', line)



                    with open("../archives/emails.txt", "a") as arquivo2:
                        if "@" in cleantext:
                            arquivo2.write(f'{parseaddr(cleantext)[1]}\n')
                        else:
                            pass

        except KeyboardInterrupt:
            print('Saindo...')

    def github(self):
        try:
            os.system(f'git clone {self.sites}.git')
        except KeyboardInterrupt:
            print('Saindo...')


if __name__ == "__main__":
    print("Tratando Dados...")
    with open("../archives/emails.txt", "w") as arquivo1:
        arquivo1.write("")
    with open("../archives/html_content.txt", "w") as arquivo:
        arquivo.write('')
    with open("../archives/site.txt", "r") as arquivo:
        for sites in arquivo:
            if "pastebin" in sites:
                url = sites
                CrawlerSites(url).pastebin()
            #if "github" in sites:
            #    url = sites
            #    CrawlerSites(url).github()


