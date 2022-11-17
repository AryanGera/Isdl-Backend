import time
import smtplib
from email.mime.text import MIMEText
i=0
#body of the mail
def sendMail(body,toaddr,subject="Recruitment Meeting Scheduled"):
    msg=MIMEText(body)
    fromaddr= "aryangera9@gmail.com" #the adress from which mail is sent # give acess to less secure apps
    # toaddr=""  # mail sent to
    msg["From"]=fromaddr     #### store the adresses into msg object
    msg["To"]=toaddr
    msg["Subject"]=subject
    server=smtplib.SMTP("smtp.gmail.com",587)   ###connect to gmail.com server using 587 port number
    server.starttls()                   #put the smtp connection in TLS mode
    server.login(fromaddr,"nmdhzzakcthaztan")  #login to your the server with the correct password
    server.send_message(msg) #send the message to the server
    print("mail sent")
    server.quit() #close the connection
    print("sleep")