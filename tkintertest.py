from tkinter import *
import csv
from random import randint
from time import gmtime, strftime
import webbrowser

root = Tk()
root.title('De NS-Fietsenstalling')
label = Label(master=root, text='Kies een van de onderstaande opties!', height=2)
label.grid()

photo = PhotoImage(file="Background_fietsenstalling.png")
photo2 = PhotoImage(file="Background_other.png")
background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

infile = open('fietsen.csv')
infile2 = open('stalling.csv')

def fiets_registreren():
    subwindow = Toplevel(master=root)
    subwindow.geometry('700x527')

    background_label = Label(subwindow, image=photo2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow,text='U heeft gekozen voor: Ik wil mijn fiets registreren.', height=1, bg='#fece22')
    label.place(x=210, y=50)

    with open('fietsen.csv', 'r', newline='') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        lijst = []

        def registreerformulier():
                voornaam = Label(master=subwindow, text="Voornaam:", bg='#fece22')
                achternaam = Label(master=subwindow, text="Achternaam: ", bg='#fece22')
                email = Label(master=subwindow, text="Email: ", bg='#fece22')
                wachtwoord = Label(master=subwindow, text="Wachtwoord: ", bg='#fece22')
                telegramidmessage = Label(master=subwindow, text="Vul hieronder uw telegram ID in als u gebruik wilt maken van two factor authentication.", bg='#fece22')
                telegramid = Label(master=subwindow, text="Telegram ID: ", bg='#fece22')

                voornaam_entry = Entry(master=subwindow)
                achternaam_entry = Entry(master=subwindow)
                email_entry = Entry(master=subwindow)
                wachtwoord_entry = Entry(master=subwindow, show="*")
                telegramid_entry = Entry(master=subwindow)

                voornaam.place(x=200, y=80)
                achternaam.place(x=200, y=110)
                email.place(x=200, y=140)
                wachtwoord.place(x=200, y=170)
                telegramidmessage.place(x=200, y=200)
                telegramid.place(x=200, y=230)

                voornaam_entry.place(x=280, y=80)
                achternaam_entry.place(x=280, y=110)
                email_entry.place(x=280, y=140)
                wachtwoord_entry.place(x=280, y=170)
                telegramid_entry.place(x=280, y=230)

                def checkregistratie():
                    if str('@') not in str(email_entry.get()) or str('.') not in str(email_entry.get()) or len(str(email_entry.get())) < 6 or len(str(email_entry.get())) > 30:
                        emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2, bg='#fece22')
                        emailcorrect.place(x=300, y=300)

                    if len(str(wachtwoord_entry.get())) < 8 or len(str(wachtwoord_entry.get())) > 12:
                        wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2, bg='#fece22')
                        wachtwoordcorrect.place(x=300, y=300)

                    elif str('@') in str(email_entry.get()) and str('.') in str(email_entry.get()) and len(str(email_entry.get())) >= 6 and len(str(email_entry.get())) <= 30 and len(str(wachtwoord_entry.get())) >= 8 and len(str(wachtwoord_entry.get())) <= 12:
                        with open('fietsen.csv', 'a', newline='') as schrijven:
                            stickercode = randint(10000, 99999)
                            stickercode2 = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode), bg='#fece22')
                            stickercode2.place(x=300, y=300)
                            writer = csv.writer(schrijven, delimiter=';')
                            writer.writerow((str(stickercode), str(voornaam_entry.get()), str(achternaam_entry.get()), str(wachtwoord_entry.get()), str(email_entry.get()), str(telegramid_entry.get())))
                            del lijst[:]
                            checkregistratieknop.config(state="disabled")

                checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie, fg='white', bg="#00246a")
                checkregistratieknop.place(x=300, y=260)

        if len(lijst) < 50 and len(lijst) != None:

            for row1 in reader:
                lijst.append(row1[0])

            if len(lijst) != 50:
                registreerformulier()


        elif len(lijst) == None and len(lijst) < 50:
            registreerformulier()

        #homeknop = Button(master=subwindow, text='Ik wil naar het hoofdmenu', command=subwindow.close_window(), fg='white', bg="red")
        #homeknop.place(x=520, y=493)

        stopknop = Button(master=subwindow, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

def fiets_stallen():
    subwindow2 = Toplevel(master=root)
    subwindow2.geometry('700x527')

    background_label = Label(subwindow2, image=photo2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow2,text='U heeft gekozen voor: Ik wil mijn fiets stallen.',height=1, bg='#fece22')
    label.place(x=210, y=50)

    stickercode = Label(master=subwindow2, text="Voer hier uw stickercode in: ", bg='#fece22')
    stickercode_entry = Entry(master=subwindow2)

    stickercode.place(x=120, y=80)
    stickercode_entry.place(x=280, y=80)

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
                            writer.writerow((str(stickercode_entry.get()), voornaam, achternaam, str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))))
                            label = Label(master=subwindow2,text='Uw fiets is gestald!',height=1, bg='#fece22')
                            label.place(x=120, y=140)
                            checkstallingknop.config(state="disabled")
                elif str(stickercode_entry.get()) not in list:
                    nietindatabase = Label(master=subwindow2,text='Deze stickercode komt niet overeen met de database!',height=1, bg='#fece22')
                    nietindatabase.place(x=120, y=140)

    checkstallingknop = Button(master=subwindow2, text='Stal fiets', command=checkstalling, fg='white', bg="#00246a")
    checkstallingknop.place(x=310, y=110)

    stopknop = Button(master=subwindow2, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
    stopknop.place(x=600, y=493)


def fiets_ophalen():
    subwindow3 = Toplevel(master=root)
    subwindow3.geometry('700x527')

    background_label = Label(subwindow3, image=photo2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow3,text='U heeft gekozen voor: Ik wil mijn fiets ophalen.',height=1, bg='#fece22')
    label.place(x=210, y=50)

    stickercode = Label(master=subwindow3, text="Voer hier uw stickercode in: ", bg='#fece22')
    stickercode_entry = Entry(master=subwindow3)
    wachtwoord = Label(master=subwindow3, text="Voer hier uw wachtwoord in: ", bg='#fece22')
    wachtwoord_entry = Entry(master=subwindow3, show="*")

    stickercode.place(x=120, y=80)
    stickercode_entry.place(x=280, y=80)
    wachtwoord.place(x=120, y=110)
    wachtwoord_entry.place(x=280, y=110)

    with open('fietsen.csv', 'r') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        list = []
        for row in reader:
            list.append(row[0])

        def checkophalen():
            if str(stickercode_entry.get()) not in list:
                nietindatabase = Label(master=subwindow3,text='Deze stickercode komt niet overeen met de database!',height=1, bg='#fece22')
                nietindatabase.place(x=120, y=170)
            elif str(stickercode_entry.get()) in list:
                with open('fietsen.csv', 'r') as lezen:
                    reader = csv.reader(lezen, delimiter=';')
                    incorrectWachtwoord = 0
                    for row in reader:
                        if row[0] == str(stickercode_entry.get()) and row[3] == str(wachtwoord_entry.get()):
                            kluisopen = Label(master=subwindow3,text='Uw fietsenkluis is open!',height=1, bg='#fece22')
                            kluisopen.place(x=120, y=170)
                            regel_verwijderen(str(stickercode_entry.get()))
                            telegramid = row[5]
                            if telegramid != '':
                                link = 'https://api.telegram.org/bot275900175:AAG2uOgInzsASLcorHUaZgMAGvvklfAIGUk/sendmessage?chat_id=' + str(telegramid) + '&text=Uw%20fiets%20is%20opgehaald%20vanaf%20de%20stalling,%20was%20u%20dit%20niet?%20bel%20dan%20snel%20naar%20onze%20helpdesk:%200900-0123456'
                                webbrowser.open(link)
                        else:
                            incorrectWachtwoord += 1
                    if incorrectWachtwoord == len(row):
                        incorrectpassword = Label(master=subwindow3,text='Incorrect wachtwoord!',height=1, bg='#fece22')
                        incorrectpassword.place(x=120, y=170)

        checkophalenknop = Button(master=subwindow3, text='Haal fiets op', command=checkophalen, fg='white', bg="#00246a")
        checkophalenknop.place(x=300, y=140)

        stopknop = Button(master=subwindow3, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

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
    subwindow4.geometry('700x527')

    background_label = Label(subwindow4, image=photo2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow4,text='U heeft gekozen voor: Ik wil informatie opvragen.',height=1, bg='#fece22')
    label.place(x=210, y=50)

    def informatie_keuze_1():
        subwindow5 = Toplevel(master=root)
        subwindow5.geometry('700x527')

        background_label = Label(subwindow5, image=photo2)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        with open('stalling.csv', 'r', newline='') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            lijst = []
            for row1 in reader:
                lijst.append(row1[0])
            stalplaatsenbezet = len(lijst)
            stalplaatsenbeschikbaar = 50 - stalplaatsenbezet
            if stalplaatsenbeschikbaar >= 1:
                stalplaatsen = Label(master=subwindow5,text='Er zijn nog ' + str(stalplaatsenbeschikbaar) + ' stalplaatsen beschikbaar.',height=1, bg='#fece22')
                stalplaatsen.place(x=210, y=50)
            if stalplaatsenbeschikbaar == 0:
                vol = Label(master=subwindow5,text='Alle stalplaatsen zijn momenteel bezet, probeer het later opnieuw.',height=1, bg='#fece22')
                vol.place(x=210, y=50)

        stopknop = Button(master=subwindow5, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

    def informatie_keuze_2():
        subwindow6 = Toplevel(master=root)
        subwindow6.geometry('700x527')

        background_label = Label(subwindow6, image=photo2)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        kosten = Label(master=subwindow6,text='De 1e dag is gratis, daarna betaal je 50 cent per dag.',height=1, bg='#fece22')
        kosten.place(x=210, y=50)

        stopknop = Button(master=subwindow6, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

    def informatie_keuze_3():
        subwindow7 = Toplevel(master=root)
        subwindow7.geometry('700x527')

        background_label = Label(subwindow7, image=photo2)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        stickercode = Label(master=subwindow7, text="Voer hier uw stickercode in: ", bg='#fece22')
        stickercode_entry = Entry(master=subwindow7)
        email = Label(master=subwindow7, text="Voer hier uw email in: ", bg='#fece22')
        email_entry = Entry(master=subwindow7)

        stickercode.place(x=140, y=80)
        stickercode_entry.place(x=300, y=80)
        email.place(x=140, y=110)
        email_entry.place(x=300, y=110)

        def checkwachtwoord():
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                email_onbekend = 0
                stickercode_onbekend = 0
                rows = 0
                for row in reader:
                    rows += 1
                    if str(email_entry.get()) == row[4] and str(stickercode_entry.get()) == row[0]:
                        wachtwoord = Label(master=subwindow7, text="Uw wachtwoord is: " + row[3], bg='#fece22')
                        wachtwoord.place(x=140, y=170)
                        telegramid = row[5]
                        if telegramid != '':
                            link = 'https://api.telegram.org/bot275900175:AAG2uOgInzsASLcorHUaZgMAGvvklfAIGUk/sendmessage?chat_id=' + str(telegramid) + '&text=Uw%20wachtwoord%20is%20opgehaald%20via%20de%20wachtwoord%20vergeten%20functie%20,%20%20was%20u%20dit%20niet?%20bel%20dan%20snel%20naar%20onze%20helpdesk:%200900-0123456'
                            webbrowser.open(link)
                    if str(email_entry.get()) != row[4]:
                        email_onbekend += 1
                    if str(stickercode_entry.get()) != row[0]:
                        stickercode_onbekend += 1
                if email_onbekend == rows:
                    email = Label(master=subwindow7, text="Het Email adres komt niet overeen met de database!", bg='#fece22')
                    email.place(x=140, y=140)
                if stickercode_onbekend == rows:
                    stickercode = Label(master=subwindow7, text="De stickercode komt niet overeen met de database!", bg='#fece22')
                    stickercode.place(x=140, y=140)

        wachtwoordknop = Button(master=subwindow7, text='Vraag mijn wachtwoord op', command=checkwachtwoord, fg='white', bg="#00246a")
        wachtwoordknop.place(x=270, y=140)

        stopknop = Button(master=subwindow7, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)


    keuze1knop = Button(master=subwindow4, text='Ik wil weten hoeveel stalplaatsen nog vrij zijn.', command=informatie_keuze_1, fg='white', bg="#00246a")
    keuze1knop.place(x=230, y=80)

    keuze2knop = Button(master=subwindow4, text='Ik wil weten wat de kosten zijn.', command=informatie_keuze_2, fg='white', bg="#00246a")
    keuze2knop.place(x=260, y=120)

    keuze3knop = Button(master=subwindow4, text='Ik ben mijn wachtwoord vergeten.', command=informatie_keuze_3, fg='white', bg="#00246a")
    keuze3knop.place(x=250, y=160)

    stopknop = Button(master=subwindow4, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
    stopknop.place(x=600, y=493)

def stoppen():
    exit()


registreerknop = Button(master=root, text='Ik wil mijn fiets registreren', command=fiets_registreren, fg='white', bg="#00246a")
registreerknop.place(x=50, y=350)

stalknop = Button(master=root, text='Ik wil mijn fiets stallen', command=fiets_stallen, fg='white', bg="#00246a")
stalknop.place(x=210, y=350)

ophaalknop = Button(master=root, text='Ik wil mijn fiets ophalen', command=fiets_ophalen, fg='white', bg="#00246a")
ophaalknop.place(x=350, y=350)

informatieopvragenknop = Button(master=root, text='Ik wil informatie opvragen', command=informatie_opvragen, fg='white', bg="#00246a")
informatieopvragenknop.place(x=500, y=350)

stopknop = Button(master=root, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
stopknop.place(x=600, y=493)


root.iconbitmap('favicon.ico')
root.geometry('700x527')
root.mainloop()
