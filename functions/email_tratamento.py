import os

email_list = []
only_users = []

print("\033[32mIsso pode levar alguns segundos...\033[m")
with open("../archives/emails.txt", "r") as arquivo:
    for linha in arquivo:
        email_list.append(linha)

with open('../archives/emails_tratados.txt', 'w') as arquivo3:
    arquivo3.write('')
    
for user in email_list:
    user = user.replace('Google', '')
    user = user.replace('Google', '')
    user = user.replace('Recovery', '')
    user = user.replace('Email', '')
    user = user.replace('Password', '')
    user = user.replace('Pass', '')
    user = user.replace(':', '')
    only_users.append(user[0:user.find("com")+3])



for user2 in only_users:
    print(user2)
    with open("../archives/emails_tratados.txt", 'a') as arquivo2:
        for c in only_users:
            arquivo2.write(f'{c}\n')


print("\033[32mPronto\033[m")



