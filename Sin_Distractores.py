import time
from datetime import datetime as dt
hora_inicio=9
minuto_inicio=29
hora_termino=10
minuto_termino=5
host_path="C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = [
    "www.facebook.com",
    "facebook.com",
    "mail.google.com",
    "youtube.com",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.youtube.com.mx/",
    "m.youtube.com",
    "https://m.facebook.com/",
    "m.facebook.com",
    "www.youtube.com"
]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hora_inicio,minuto_inicio) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hora_termino,minuto_termino):
        print("working")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() 
        print("toy dormido")
    time.sleep(1)