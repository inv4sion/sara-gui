import os
import json

emails = []

with open("../archives/emails.txt", "r") as arquivo:
    for line in arquivo:
        emails.append(line)

with open("../data/data_bd.json", "w") as write_file:
    json.dump(emails, write_file, indent=4)

