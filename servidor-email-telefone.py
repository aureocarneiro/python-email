import socket
import sys
import threading
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

UDP_PORT = int(17003)
mail_de = ("")
mail_para = ("")
mail_msgm = ("")
mail_sub = ("")
mail_pass = ("")

msg = MIMEMultipart()
msg['From'] = mail_para
msg['To'] = mail_de
msg['Subject'] = mail_sub
message = mail_msgm
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(mail_de, mail_pass)

mailserver.sendmail(mail_de,mail_para,msg.as_string())

mailserver.quit()


