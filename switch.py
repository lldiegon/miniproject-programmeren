import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(12, GPIO.HIGH)

tr = 0
code = 1234
knipperkeuze = 1

def wait():
    time.sleep(0.5)

def waitlong():
    time.sleep(1)

while True:
    if GPIO.input(21) == False:
        tr = 1
        #print("1")
    #print(tr)
    if GPIO.input(16) == False:
        #print('wat is tr', tr)
        invoer=input("Vul de beveiligingscode in: ")
        if invoer == code:
            print("Code correct!")
            print("1: Alarm resetten")
            print("2: Alarm knippermodus selecteren")
            keuze = input("Kies een van de bovenstaande nummers: ")
            if keuze == 1:
                print("Alarm gereset!")
                tr = 0
            if keuze == 2:
                print("1: Constant aan")
                print("2: Snel knipperen")
                print("3: Langzaam knipperen")
                knipperkeuze = input("Kies een van de bovenstaande knippermodes")
                if knipperkeuze <= 3 and knipperkeuze >= 1:
                    print("Wijzigen gelukt!")
                else:
                    print("Fout, kies een van de bovenstaande opties!")
                    knipperkeuze = input("Kies een van de bovenstaande knippermodes")
        else:
            print("Code incorrect!")
            invoer=input("Vul de beveiligingscode in: ")
            tr = 1

    if tr == 1 and knipperkeuze == 1:
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
    if tr == 1 and knipperkeuze == 2:
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            wait()
            GPIO.output(18, GPIO.LOW)
            wait()
    if tr == 1 and knipperkeuze == 3:
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            waitlong()
            GPIO.output(18, GPIO.LOW)
            waitlong()
    if tr == 0:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
