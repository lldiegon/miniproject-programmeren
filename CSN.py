import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(12, GPIO.HIGH)

tr = 0
code = 1234
knipperkeuze = 1
buzzer = 0
buzzerconfig = 2

def wait():
    time.sleep(0.5)

def waitlong():
    time.sleep(1)

while True:
    #hier wordt gecheckt of er op knoppen gedrukt word.
    if GPIO.input(21) == False:
        tr = 1
    elif GPIO.input(16) == False:
        invoer=input("Vul de beveiligingscode in: ")
        if invoer == code:
            #Als de code correct is wordt er een nieuw keuze menu gepresenteerd 
            print("Code correct!")
            print("1: Alarm resetten")
            print("2: Alarm knippermodus selecteren")
            print("3: Alarm buzzer aan of uit zetten")
            keuze = input("Kies een van de bovenstaande nummers: ")
            if keuze == 1:
                # deze keuze zet het alarm weer uit
                print("Alarm gereset!")
                tr = 0
            elif keuze == 2:
                # het alarm kan snel of kort knipperen, hier wordt dat gekozen
                print("1: Constant aan")
                print("2: Snel knipperen")
                print("3: Langzaam knipperen")
                knipperkeuze = input("Kies een van de bovenstaande knippermodes")
                if knipperkeuze <= 3 and knipperkeuze >= 1:
                    print("Wijzigen gelukt!")
                else:
                    # keuze is fout
                    print("Fout, kies een van de bovenstaande opties!")
                    knipperkeuze = input("Kies een van de bovenstaande knippermodes")
                    continue
            elif keuze == 3:
                # hiermee wordt de buzzer aan of uit gezet
                print("1: Buzzer aan")
                print("2: Buzzer uit")
                buzzerconfig = input("Kies een van de bovenstaande knippermodes")
                if knipperkeuze <= 2 and knipperkeuze >= 1:
                    print("Wijzigen gelukt!")
                else:
                    print("Fout, kies een van de bovenstaande opties!")
                    knipperkeuze = input("Kies een van de bovenstaande knippermodes")
        elif invoer != code:
            # code is incorrect en gaat weer terug naar het invoeren van de code 
            print("Code incorrect!")
            tr = 1

    elif tr == 1 and knipperkeuze == 1:
        # Het lampje staat nu constant aan
        buzzer = buzzerconfig
        if buzzer == 1:
            GPIO.output(23, GPIO.HIGH)
        elif buzzer == 2:
            GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    elif tr == 1 and knipperkeuze == 2:
        # het lampje knippert nu snel
        buzzer = buzzerconfig
        if buzzer == 1:
            GPIO.output(23, GPIO.HIGH)
        elif buzzer == 2:
            GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        wait()
        GPIO.output(18, GPIO.LOW)
        wait()
        GPIO.output(18, GPIO.HIGH)
    elif tr == 1 and knipperkeuze == 3:
        # het lampje knippert nu langzaam 
        buzzer = buzzerconfig
        if buzzer == 1:
            GPIO.output(23, GPIO.HIGH)
        elif buzzer == 2:
            GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        waitlong()
        GPIO.output(18, GPIO.LOW)
        waitlong()
        GPIO.output(18, GPIO.HIGH)
    elif tr == 0:
        buzzer = 2
        GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)


