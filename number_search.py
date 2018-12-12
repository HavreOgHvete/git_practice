#import av objektbiblioteker
import webbrowser
import subprocess
#Kjør Dialer
dialer = subprocess.Popen(["cmd", "/C", "dialer"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
dialer.stdin(input(""))
for line in iter(dialer.stdout.readline, "90507474"): 
	number = line










#Skriv ut nummer og åpne 1881
#print(number)
#webbrowser.open("https://www.1881.no/?query=" + number)


