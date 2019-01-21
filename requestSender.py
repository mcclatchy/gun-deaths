# #!/usr/bin/python
# import the libraries we need
import json
from smtplib import SMTP # Standard connection
from smtplib import SMTP_SSL as SMTP #SSL connection
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pygsheets
import pandas as pd
import gspread
from datetime import date, timedelta
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
today = date.today()
today = str(today.strftime('%m/%d/%y'))
#authorization to login to Google Sheets
login = pygsheets.authorize(service_file='creds.json')

#open the google spreadsheet (where 'GunDeathMinorsPRRTracker' is the name of my sheet)
sheet = login.open('GunDeathMinorsPRRTracker').sheet1
#get all of the data in that sheet
data = sheet.get_all_records()
i = 1
print(data)
for datum in data:
    time.sleep(4)
    # make a variable called i. each time we look at a new row, we're going to count which row we're on
    i += 1
    #identify variables within the sheet
    date = datum['Date of Incident'].encode('utf-8').strip()
    name = datum["Victim's Name"].encode('utf-8').strip()
    address = datum['Street Address'].encode('utf-8').strip()
    city = datum['City'].encode('utf-8').strip()
    state = datum['State'].encode('utf-8').strip()
    email = datum['email'].encode('utf-8').strip()
    statute = datum['statute'].encode('utf-8').strip()
    request_sent = datum['request_sent'].encode('utf-8').strip()
    date_sent = datum['date_sent'].encode('utf-8').strip()
    sender = '{EMAIL ADDRESS}'
    receivers = [email]
    #if there is an email listed
    if (email is not ''):
        #and if I have not sent a request already AND I know the name of the victim, use this email template
        if (request_sent is '') & (name is ''):
            msg = MIMEMultipart()
            msg['From'] = '{EMAIL ADDRESS}'
            msg['To'] = email
            msg['Subject'] = '{SUBJECT LINE}'
            message = "{MESSAGE with relevant statute and information passed in if we don't know the name of the victim}"
            msg.attach(MIMEText(message))

            ServerConnect = False
            #Try and send it, else something is not right
            try:
                smtp_server = SMTP('smtp.gmail.com','465')
                smtp_server.login('EMAIL ADDRESS', 'EMAIL PASSWORD')
                ServerConnect = True
            except SMTPHeloError as e:
                print "Server did not reply"
            except SMTPAuthenticationError as e:
                print "Incorrect username/password combination"
            except SMTPException as e:
                print "Authentication failed"

            if ServerConnect == True:
                try:
                    #update my sheet to say the request was sent of the matching line
                    request_sent = ('B%d' %i)
                    date_sent = ('A%d' %i)
                    smtp_server.sendmail(sender, receivers, msg.as_string())
                    sheet.update_cell(str(request_sent), 'Sent')
                    sheet.update_cell(str(date_sent), today)
                except SMTPException as e:
                    print "Error: unable to send email", e
                finally:
                    smtp_server.close()
        # if I have not sent a request already AND I know the name of the victim, use this template
        elif (request_sent is '') & (name is not ''):
            msg = MIMEMultipart()
            msg['From'] = '{EMAIL ADDRESS}'
            msg['To'] = email
            msg['Subject'] = '{SUBJECT LINE}'
            message = "{MESSAGE with relevant statute and information passed in if we do know the name of the victim}"
            msg.attach(MIMEText(message))

            ServerConnect = False
            try:
                smtp_server = SMTP('smtp.gmail.com','465')
                smtp_server.login('EMAIL ADDRESS', 'EMAIL PASSWORD')
                ServerConnect = True
            except SMTPHeloError as e:
                print "Server did not reply"
            except SMTPAuthenticationError as e:
                print "Incorrect username/password combination"
            except SMTPException as e:
                print "Authentication failed"

            if ServerConnect == True:
                try:
                    #update my sheet to say the request was sent of the matching line
                    request_sent = ('B%d' %i)
                    date_sent = ('A%d' %i)
                    smtp_server.sendmail(sender, receivers, msg.as_string())
                    sheet.update_cell(str(request_sent), 'Sent')
                    sheet.update_cell(str(date_sent), today)
                except SMTPException as e:
                    print "Error: unable to send email", e
                finally:
                    smtp_server.close()
        else:
            print("Nothing to do here")
