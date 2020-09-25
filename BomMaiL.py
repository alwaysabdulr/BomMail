#!/usr/bin/python
#BomMail

import os
import smtplib
import getpass
import sys
import time
import random

print """

 /$$$$$$$                          /$$      /$$           /$$ /$$      
| $$__  $$                        | $$$    /$$$          |__/| $$      
| $$  \ $$  /$$$$$$  /$$$$$$/$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$      
| $$$$$$$  /$$__  $$| $$_  $$_  $$| $$ $$/$$ $$ |____  $$| $$| $$      
| $$__  $$| $$  \ $$| $$ \ $$ \ $$| $$  $$$| $$  /$$$$$$$| $$| $$      
| $$  \ $$| $$  | $$| $$ | $$ | $$| $$\  $ | $$ /$$__  $$| $$| $$      
| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$ \/  | $$|  $$$$$$$| $$| $$$$$$$$
|_______/  \______/ |__/ |__/ |__/|__/     |__/ \_______/|__/|________/
                                                                                
"""
def BomEmail():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

server = raw_input ('MailServer 1.Gmail/2.Yahoo: ')
user = raw_input('Email: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTo: ')
subjectnumber=input('how many subjects do you have: ')
subjectlist=[]
for n in range(subjectnumber):
	subject = raw_input('Subject: ')
	subjectlist.append(subject)
	n+=1

numberofentry=int(input('how many different text do you want to send: '))
list=[]
for i in range(numberofentry):

	body = raw_input('Message: ')
	list.append(body)
	i+=1
total = input('Number of send: ')

if server == 'gmail' or '1' or 'Gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo' or '2' or 'Yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Kindly Enter Your Answer in 1 or 2 in Mail Server.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        random_num = random.choice(list)
	random_text=random.choice(subjectlist) 
       
	msg = 'From: ' + user + '\nSubject: ' + random_text + '\n' +random_num 
        server.sendmail(user,to,msg)
        print "\r[+]E-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done  !!!'
    print '                                                  BomMail :~ Enjoy :)'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps'
    sys.exit()
