#import av objektbiblioteker
import webbrowser
import subprocess
#Kjør Dialer
dialer = subprocess.Popen(["cmd", "/C", "dialer"], stdout=subprocess.PIPE)
#Sjekk Dialer for eksisterende output

number = input(dialer.communicate())


#Mangler korrekt subprocess-metode
print(number)
#Om output finnes: åpne 1881.no med søk etter output
webbrowser.open("https://www.1881.no/?query=" + number)
number = input("Next number ")
number = str(dialer.communicate(number))
#For å hindre evig looping under testing: IKKE RØR før 
#stabil verson
#er ferdig!
