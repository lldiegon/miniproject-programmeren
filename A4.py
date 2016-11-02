import csv
from random import randint
from datetime import datetime

infile = open('fietsen.csv')
infile2 = open('stalling.csv')
lezen = infile.read()

while True:
    print("1: Ik wil mijn fiets registreren")
    print("2: Ik wil mijn fiets stallen")
    print("3: Ik wil mijn fiets ophalen")
    print("4: Ik wil informatie opvragen")
    print("5: Ik wil stoppen")
    break

def invoer():
    keuze = int(input("Kies een van de bovenstaande opties door een nummer in te voeren: "))
    if keuze == 1:
        fiets_registreren()

    if keuze == 2:
        fiets_stallen()

    if keuze == 3:
        fiets_ophalen()

    if keuze == 4:
        informatie_opvragen()

    if keuze == 5:
        stoppen()

    while keuze < 1 or keuze > 5:
        print("U heeft een verkeerd nummer ingevuld, kies een nummer tussen de 1 en 4")
        keuze = input("Kies een van de bovenstaande opties door een nummer in te voeren: ")

def fiets_registreren():
    print("U heeft gekozen voor: Ik wil mijn fiets registreren.")
    print("Je krijgt een fietsenkluis met een unieke code als deze beschikbaar is.")
    with open('fietsen.csv', 'r', newline='') as lezen:
        with open('fietsen.csv', 'a', newline='') as schrijven:
            reader = csv.reader(lezen, delimiter=';')
            lijst = []
            if len(lijst) < 50 and len(lijst) != None:

                for row1 in reader:
                    lijst.append(row1[0])

                if len(lijst) != 50:
                    writer = csv.writer(schrijven, delimiter=';')
                    voornaam = str(input("Vul uw voornaam in: "))
                    achternaam = str(input("Vul uw achternaam in: "))

                    stickercode = randint(10000, 99999)
                    print('Uw stickercode is: ' + str(stickercode))
                    email = str(input("Vul uw email in: "))

                    while str('@') not in email or str('.') not in email or len(email) < 6 or len(email) > 30:
                        print("Dit is geen geldig email adres!")
                        email = str(input("Vul uw email in: "))

                    wachtwoord = str(input("Vul een wachtwoord in: "))

                    while len(wachtwoord) < 8 or len(wachtwoord) > 12:
                        print("Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!")
                        wachtwoord = str(input("Vul een wachtwoord in: "))

                    writer.writerow((stickercode, voornaam, achternaam, wachtwoord, email))
                    del lijst[:]

                else:
                    print('Alle stalplaatsen zijn momenteel in gebruik, probeer het later opnieuw.')

            elif len(lijst) == None and len(lijst) < 50:
                writer = csv.writer(schrijven, delimiter=';')
                voornaam = str(input("Vul uw voornaam in: "))
                achternaam = str(input("Vul uw achternaam in: "))

                stickercode = randint(10000, 99999)
                print('Uw stickercode is: ' + str(stickercode))
                email = str(input("Vul uw email in: "))

                while str('@') not in email or str('.') not in email or len(email) < 6 or len(email) > 30:
                    print("Dit is geen geldig email adres!")
                    email = str(input("Vul uw email in: "))

                wachtwoord = str(input("Vul een wachtwoord in: "))

                while len(wachtwoord) < 8 or len(wachtwoord) > 12:
                    print("Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!")
                    wachtwoord = str(input("Vul een wachtwoord in: "))

                writer.writerow((stickercode, voornaam, achternaam, wachtwoord, email))

def fiets_stallen():
    print("U heeft gekozen voor: Ik wil mijn fiets stallen.")
    with open('stalling.csv', 'a', newline='') as schrijven:
        with open('fietsen.csv', 'r') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            list = []
            stickercode = int(input('Voer uw stickercode in: '))
            for row in reader:
                    list.append(row[0])
            if stickercode in list:
                    writer = csv.writer(schrijven, delimiter=';')
                    if row[0] == stickercode:
                        voornaam = row[1]
                        achternaam = row[2]
                        writer.writerow((stickercode, voornaam, achternaam, str(datetime.now())))
                        print("Uw fiets is gestalt!")
            elif stickercode not in list:
                print("Deze stickercode komt niet overeen met de database!")

def fiets_ophalen():
    print("U heeft gekozen voor: Ik wil mijn fiets ophalen.")
    stickercode = input('Voer uw stickercode in: ')

    with open('fietsen.csv', 'r') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        list = []
        for row in reader:
            list.append(row[0])
        if stickercode not in list:
            print('Deze stickercode komt niet overeen met de database!')
        elif stickercode in list:
            wachtwoord = input('Voer uw bijbehorende wachtwoord in: ')
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                for row in reader:
                    if row[0] == stickercode and row[3] == wachtwoord:
                        print('Kluis is open')
                    if row[0] == stickercode and row[3] != wachtwoord:
                        print('Wachtwoord is incorrect')

def informatie_opvragen():
    print("U heeft gekozen voor: Ik wil informatie opvragen.")

    print("1: Ik wil weten hoeveel stalplaatsen er nog beschikbaar zijn.")
    print("2: Ik wil weten hoeveel het kost om mijn fiets te stallen.")
    print("3: Ik ben mijn wachtwoord vergeten.")
    keuzes = [1, 2, 3]
    informatie_keuze = int(input('Vul een nummer voor de keuze in: '))

    while informatie_keuze not in keuzes:
        print('Dit is geen optie, kies opnieuw')
        informatie_keuze = int(input('Vul een nummer voor de keuze in: '))

    if informatie_keuze == 1:
        with open('stalling.csv', 'r', newline='') as lezen:
            with open('stalling.csv', 'a', newline='') as schrijven:
                reader = csv.reader(lezen, delimiter=';')
                lijst = []
                print("U heeft gekozen voor: Ik wil weten hoeveel stalplaatsen nog vrij zijn.")
                for row1 in reader:
                    lijst.append(row1[0])
                stalplaatsenbezet = len(lijst)
                stalplaatsenbeschikbaar = 50 - stalplaatsenbezet
                if stalplaatsenbeschikbaar >= 1:
                    print('Er zijn nog ' + str(stalplaatsenbeschikbaar) + ' stalplaatsen beschikbaar.')
                if stalplaatsenbeschikbaar == 0:
                    print('Alle stalplaatsen zijn momenteel bezet, probeer het later opnieuw.')

    if informatie_keuze == 2:
        print("De 1e dag is gratis, daarna betaal je 50 cent per dag.")

    if informatie_keuze == 3:
        mail = input(print('Wat is uw email?:'))
        stickercode = input(print('Wat is de stickercode?:'))

        with open('fietsen.csv', 'r') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            list = []
            for row in reader:
                if mail == row[3] and stickercode == row[0]:
                    print('Uw wachtwoord is:', row[4])

def stoppen():
    print("U heeft gekozen voor: Ik wil stoppen.")

invoer()
