import time
import smtplib
from email.mime.text import MIMEText
i=0

def sendMail(body,toaddr,subject):
    msg=MIMEText(body)
    fromaddr= "hepi.monke@gmail.com" 
    
    msg["From"]=fromaddr     
    msg["To"]=toaddr
    msg["Subject"]=subject
    server=smtplib.SMTP("smtp.gmail.com",587)   
    server.starttls()                   
    server.login(fromaddr,"miuzvrcqwxcvviis")  
    server.send_message(msg) 
    print("mail sent")
    server.quit() 
    print("sleep")