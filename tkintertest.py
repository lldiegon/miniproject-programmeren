from tkinter import *
import csv
from random import randint
from datetime import datetime
import webbrowser

root = Tk()
root.title('De NS-Fietsenstalling')
label = Label(master=root, text='Kies een van de onderstaande opties!', height=2)
label.grid()

photo = PhotoImage(file="das fiets.png")
background_label = Label(root, image=photo)
background_label.grid()
background_label.place(x=0, y=0, relwidth=1, relheight=1)

infile = open('fietsen.csv')
infile2 = open('stalling.csv')

def fiets_registreren():
    subwindow = Toplevel(master=root)
    subwindow.geometry('575x390')

    background_label = Label(subwindow, image=photo)
    background_label.grid()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow,text='U heeft gekozen voor: Ik wil mijn fiets registreren.',height=1)
    label.grid(row=0, column=2)

    with open('fietsen.csv', 'r', newline='') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        lijst = []
        if len(lijst) < 50 and len(lijst) != None:

            for row1 in reader:
                lijst.append(row1[0])

            if len(lijst) != 50:
                voornaam = Label(master=subwindow, text="Voornaam")
                achternaam = Label(master=subwindow, text="Achternaam")
                email = Label(master=subwindow, text="Email")
                wachtwoord = Label(master=subwindow, text="wachtwoord")

                voornaam_entry = Entry(master=subwindow)
                achternaam_entry = Entry(master=subwindow)
                email_entry = Entry(master=subwindow)
                wachtwoord_entry = Entry(master=subwindow, show="*")

                voornaam.grid(row=1, column=1, sticky=E)
                achternaam.grid(row=2, column=1, sticky=E)
                email.grid(row=3, column=1, sticky=E)
                wachtwoord.grid(row=4, column=1, sticky=E)

                voornaam_entry.grid(row=1, column=2)
                achternaam_entry.grid(row=2, column=2)
                email_entry.grid(row=3, column=2)
                wachtwoord_entry.grid(row=4, column=2)



                def checkregistratie():
                    if str('@') not in str(email_entry.get()) or str('.') not in str(email_entry.get()) or len(str(email_entry.get())) < 6 or len(str(email_entry.get())) > 30:
                        emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2)
                        emailcorrect.grid(row=6, column=2)

                    if len(str(wachtwoord_entry.get())) < 8 or len(str(wachtwoord_entry.get())) > 12:
                        wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2)
                        wachtwoordcorrect.grid(row=6, column=2)
                    elif str('@') in str(email_entry.get()) and str('.') in str(email_entry.get()) and len(str(email_entry.get())) >= 6 and len(str(email_entry.get())) <= 30 and len(str(wachtwoord_entry.get())) >= 8 and len(str(wachtwoord_entry.get())) <= 12:
                        with open('fietsen.csv', 'a', newline='') as schrijven:
                            stickercode = randint(10000, 99999)
                            stickercode2 = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode))
                            stickercode2.grid(row=5, column=3, sticky=E)
                            writer = csv.writer(schrijven, delimiter=';')
                            writer.writerow((str(stickercode), str(voornaam_entry.get()), str(achternaam_entry.get()), str(wachtwoord_entry.get()), str(email_entry.get())))
                            del lijst[:]
                            checkregistratieknop.config(state="disabled")

                checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie)
                checkregistratieknop.grid(row=5, column=2)

            else:
                vol = Label(master=subwindow, text='Alle stalplaatsen zijn momenteel in gebruik, probeer het later opnieuw.')
                vol.grid(row=4, column=2)

        elif len(lijst) == None and len(lijst) < 50:
            voornaam = Label(master=subwindow, text="Voornaam")
            achternaam = Label(master=subwindow, text="Achternaam")
            email = Label(master=subwindow, text="Email")
            wachtwoord = Label(master=subwindow, text="wachtwoord")

            voornaam_entry = Entry(master=subwindow)
            achternaam_entry = Entry(master=subwindow)
            email_entry = Entry(master=subwindow)
            wachtwoord_entry = Entry(master=subwindow, show="*")

            voornaam.grid(row=1, column=1, sticky=E)
            achternaam.grid(row=2, column=1, sticky=E)
            email.grid(row=3, column=1, sticky=E)
            wachtwoord.grid(row=4, column=1, sticky=E)

            voornaam_entry.grid(row=1, column=2)
            achternaam_entry.grid(row=2, column=2)
            email_entry.grid(row=3, column=2)
            wachtwoord_entry.grid(row=4, column=2)

            def checkregistratie():
                if str('@') not in str(email_entry.get()) or str('.') not in str(email_entry.get()) or len(str(email_entry.get())) < 6 or len(str(email_entry.get())) > 30:
                    emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2)
                    emailcorrect.grid(row=2, column=2)

                if len(str(wachtwoord_entry.get())) < 8 or len(str(wachtwoord_entry.get())) > 12:
                    wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2)
                    wachtwoordcorrect.grid(row=3, column=2)

                elif str('@') in str(email_entry.get()) and str('.') in str(email_entry.get()) and len(str(email_entry.get())) >= 6 and len(str(email_entry.get())) <= 30 and len(str(wachtwoord_entry.get())) >= 8 and len(str(wachtwoord_entry.get())) <= 12:
                    with open('fietsen.csv', 'a', newline='') as schrijven:
                        stickercode = randint(10000, 99999)
                        stickercode2 = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode))
                        stickercode2.grid(row=5, column=3, sticky=E)
                        writer = csv.writer(schrijven, delimiter=';')
                        writer.writerow((str(stickercode), str(voornaam_entry.get()), str(achternaam_entry.get()), str(wachtwoord_entry.get()), str(email_entry.get())))
                        del lijst[:]
                        checkregistratieknop.config(state="disabled")

            checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie)
            checkregistratieknop.grid(row=4, column=1)

def fiets_stallen():
    subwindow2 = Toplevel(master=root)
    subwindow2.geometry('575x390')

    background_label = Label(subwindow2, image=photo)
    background_label.grid()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow2,text='U heeft gekozen voor: Ik wil mijn fiets stallen.',height=1)
    label.grid(row=0, column=2)

    stickercode = Label(master=subwindow2, text="Voor hier uw stickercode in: ")
    stickercode_entry = Entry(master=subwindow2)

    stickercode.grid(row=1, column=1, sticky=E)
    stickercode_entry.grid(row=1, column=2, sticky=E)

    def checkstalling():
        with open('stalling.csv', 'a', newline='') as schrijven:
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                list = []
                for row in reader:
                        list.append(row[0])
                if str(stickercode_entry.get()) in list:
                        writer = csv.writer(schrijven, delimiter=';')
                        if row[0] == str(stickercode_entry.get()):
                            voornaam = row[1]
                            achternaam = row[2]
                            writer.writerow((str(stickercode_entry.get()), voornaam, achternaam, str(datetime.now())))
                            label = Label(master=subwindow2,text='Uw fiets is gestalt!',height=1)
                            label.grid(row=2, column=2)
                            checkstallingknop.config(state="disabled")
                elif str(stickercode_entry.get()) not in list:
                    nietindatabase = Label(master=subwindow2,text='Deze stickercode komt niet overeen met de database!',height=1)
                    nietindatabase.grid(row=2, column=2)

    checkstallingknop = Button(master=subwindow2, text='Stal fiets', command=checkstalling)
    checkstallingknop.grid(row=4, column=1)


def fiets_ophalen():
    subwindow3 = Toplevel(master=root)
    subwindow3.geometry('575x390')

    background_label = Label(subwindow3, image=photo)
    background_label.grid()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow3,text='U heeft gekozen voor: Ik wil mijn fiets ophalen.',height=1)
    label.grid(row=0, column=2)

    stickercode = Label(master=subwindow3, text="Voor hier uw stickercode in: ")
    stickercode_entry = Entry(master=subwindow3)
    wachtwoord = Label(master=subwindow3, text="wachtwoord")
    wachtwoord_entry = Entry(master=subwindow3, show="*")

    stickercode.grid(row=1, column=1, sticky=E)
    stickercode_entry.grid(row=1, column=2, sticky=E)
    wachtwoord.grid(row=2, column=1, sticky=E)
    wachtwoord_entry.grid(row=2, column=2)

    with open('fietsen.csv', 'r') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        list = []
        for row in reader:
            list.append(row[0])

        def checkophalen():
            if str(stickercode_entry.get()) not in list:
                nietindatabase = Label(master=subwindow3,text='Deze stickercode komt niet overeen met de database!',height=1)
                nietindatabase.grid(row=3, column=2)
            elif str(stickercode_entry.get()) in list:
                with open('fietsen.csv', 'r') as lezen:
                    reader = csv.reader(lezen, delimiter=';')
                    for row in reader:
                        if row[0] == str(stickercode_entry.get()) and row[3] == str(wachtwoord_entry.get()):
                            kluisopen = Label(master=subwindow3,text='Uw fietsenkluis is open!',height=1)
                            kluisopen.grid(row=2, column=2)
                            regel_verwijderen(str(stickercode_entry.get()))

                        if row[3] != str(wachtwoord_entry.get()):
                            incorrectpassword = Label(master=subwindow3,text='Incorrect wachtwoord!',height=1)
                            incorrectpassword.grid(row=3, column=2)

        checkophalenknop = Button(master=subwindow3, text='Haal fiets op', command=checkophalen)
        checkophalenknop.grid(row=3, column=1)

def regel_verwijderen(stickercode):
    with open('stalling.csv', 'r') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        stickercodes = []
        voornamen = []
        achternamen = []
        datums = []
        for row in reader:
            if row[0] != str(stickercode):
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

def informatie_opvragen():
    subwindow4 = Toplevel(master=root)
    subwindow4.geometry('575x390')

    background_label = Label(subwindow4, image=photo)
    background_label.grid()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow4,text='U heeft gekozen voor: Ik wil informatie opvragen.',height=1)
    label.grid(row=0, column=2)

    def informatie_keuze_1():
        with open('stalling.csv', 'r', newline='') as lezen:
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

    def informatie_keuze_2():
        print("De 1e dag is gratis, daarna betaal je 50 cent per dag.")

    def informatie_keuze_3():
        mail = input(print('Wat is uw email?:'))
        stickercode = input(print('Wat is de stickercode?:'))

        with open('fietsen.csv', 'r') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            list = []
            for row in reader:
                if mail == row[3] and stickercode == row[0]:
                    print('Uw wachtwoord is:', row[4])


    keuze1knop = Button(master=root, text='Ik wil weten hoeveel stalplaatsen nog vrij zijn.', command=informatie_keuze_1)
    keuze1knop.grid(row=0, column=1)

    keuze2knop = Button(master=root, text='Ik wil weten wat de kosten zijn.', command=informatie_keuze_2)
    keuze2knop.grid(row=1, column=1)

    keuze3knop = Button(master=root, text='Ik ben mijn wachtwoord vergeten.', command=informatie_keuze_3)
    keuze3knop.grid(row=2, column=1)

def stoppen():
    print("U heeft gekozen voor: Ik wil stoppen.")


registreerknop = Button(master=root, text='Ik wil mijn fiets registreren', command=fiets_registreren)
registreerknop.grid(row=0, column=1)

stalknop = Button(master=root, text='Ik wil mijn fiets stallen', command=fiets_stallen)
stalknop.grid(row=1, column=1)

ophaalknop = Button(master=root, text='Ik wil mijn fiets ophalen', command=fiets_ophalen)
ophaalknop.grid(row=2, column=1)

informatieopvragenknop = Button(master=root, text='Ik wil informatie opvragen', command=informatie_opvragen)
informatieopvragenknop.grid(row=3, column=1)

stopknop = Button(master=root, text='Ik wil stoppen', command=stoppen)
stopknop.grid(row=4, column=1)


root.geometry('575x390')
root.mainloop()
