"""GUI voor het miniproject met behulp van tkinter
problemen:  -hoe ervoor te zorgen dat als je op bijv. 'registreer' drukt de functie fiets_registreren(self) wordt uitgevoerd in de window van tkinter en niet in pycharm
            -een achtergrond te krijgen, ik heb een foto en ik heb 3labes waar je je gevens in kan voeren maar de foto overlapt de 3labels"""

#importeert alles van de tkinter module
from tkinter import *
import csv
from random import randint
from datetime import datetime

infile = open('fietsen.csv')
infile2 = open('stalling.csv')
lezen = infile.read()
#creeërt hier de root window
root = Tk()

# we maken een class genaamd Window aan, deze heeft alle gegevens die in class Frame zit van tkinter
# je creeërt hiermee een leeg venster. Dit is de master(parent) window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        self.voornaam = Label(self, text="Voornaam")
        self.achternaam = Label(self, text="Achternaam")
        self.wachtwoord = Label(self, text="wachtwoord")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self)
        self.entry_3 = Entry(self, show="*")

        self.voornaam.grid(row=0, sticky=E)
        self.achternaam.grid(row=1, sticky=E)
        self.wachtwoord.grid(row=2, sticky=E)

        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)

    def init_window(self):
        #geeft de master window zijn naam
        self.master.title('De NS-Fietsenstalling')
        self.pack(fill=BOTH, expand=1)
        #creërt een menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #maakt registreren deel van het menu, het voert de functie fiets_registreren(self) uit
        registreren = Menu(menu)
        registreren.add_command(label='Registreer', command=self.fiets_registreren)
        menu.add_cascade(label="Registreren", menu=registreren)

        #maakt stallen deel van het menu, het voert de functie fiets_stallen(self) uit
        stallen = Menu(menu)
        stallen.add_command(label='Fiets stallen', command=self.fiets_stallen)
        menu.add_cascade(label='Stallen', menu=stallen)

        #maakt ophalen deel van het menu, het voert de functie fiets_ophalen(self) uit
        ophalen = Menu(menu)
        ophalen.add_command(label='Fiets Ophalen', command=self.fiets_ophalen)
        menu.add_cascade(label='Ophalen', menu=ophalen)

        #maakt informatie deel van het menu, het voert de functie informatie_opvragen(self) uit
        informatie = Menu(menu)
        informatie.add_command(label='Informatie', command=self.informatie_opvragen)
        menu.add_cascade(label='Informatie', menu=informatie)

        #maakt stoppen deel van het menu, het voert de functie client_exit(self) uit
        stoppen = Menu(menu)
        stoppen.add_command(label='Sluit', command=self.client_exit)
        menu.add_cascade(label='Stoppen', menu=stoppen)

    def fiets_registreren(self):
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

    def fiets_stallen(self):
        print("U heeft gekozen voor: Ik wil mijn fiets stallen.")
        stickercode = input('Voer uw stickercode in: ')

        with open('stalling.csv', 'a', newline='') as schrijven:
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                list = []
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

    def fiets_ophalen(self):
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
                            regel_verwijderen(stickercode)
                        if row[0] == stickercode and row[3] != wachtwoord:
                            print('Wachtwoord is incorrect')
    def regel_verwijderen(stickercode):
        with open('stalling.csv', 'r') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            stickercodes = []
            voornamen = []
            achternamen = []
            datums = []
            for row in reader:
                if row[0] != stickercode:
                    stickercodes.append(row[0])
                    voornamen.append(row[1])
                    achternamen.append(row[2])
                    datums.append(row[3])

        with open('stalling.csv', 'w', newline='') as schrijven:
            writer = csv.writer(schrijven, delimiter=';')
            i = 0
            while i < len(stickercodes):
                writer.writerow((stickercodes[i] , voornamen[i], achternamen[i], datums[i]))
                i = i + 1


    def informatie_opvragen(self):
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

    def client_exit(self):
        exit()


#voegt het ns icoon toe als icoon van de window
root.iconbitmap('favicon.ico')
#voegt een foto toe
photo = PhotoImage(file="das fiets.png")
label = Label(root, image=photo)
label.pack()


#bepaalt de grote van de window in eerste instantie
root.geometry('575x390')

app = Window(root)
#mainloop
root.mainloop()
