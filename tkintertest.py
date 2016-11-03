from tkinter import *
import csv
from random import randint
from datetime import datetime

root = Tk()
label = Label(master=root, text='Kies een van de onderstaande opties!', height=2)
label.pack()

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


registreerknop = Button(master=root, text='Ik wil mijn fiets registreren', command=fiets_registreren)
registreerknop.pack(pady=10)

stalknop = Button(master=root, text='Ik wil mijn fiets stallen')
stalknop.pack(pady=10)

ophaalknop = Button(master=root, text='Ik wil mijn fiets ophalen')
ophaalknop.pack(pady=10)

informatieopvragenknop = Button(master=root, text='Ik wil informatie opvragen')
informatieopvragenknop.pack(pady=10)

stopknop = Button(master=root, text='Ik wil stoppen')
stopknop.pack(pady=10)


root.geometry('575x390')
root.mainloop()
