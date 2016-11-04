from tkinter import *
import csv
from random import randint
from time import gmtime, strftime
import webbrowser

"""root file wordt aangemaakt, dit is de main window."""
root = Tk()
root.title('De NS-Fietsenstalling')
"""Geeft de shell de naam De NS-Fietsenstalling."""
label = Label(master=root, text='Kies een van de onderstaande opties!', height=2)
label.grid()

photo = PhotoImage(file="Background_fietsenstalling.png")
photo2 = PhotoImage(file="Background_other.png")
"""Geeft de shell de foto das fiets.png als achtergrond."""
background_label = Label(root, image=photo)
background_label.place(x=0, y=0)
"""zorgt ervoor dat de foto op de achtergrond zit."""

infile = open('fietsen.csv')
infile2 = open('stalling.csv')
"""Openen van de CSV files."""

def fiets_registreren():
    """Functie fiets registreren."""
    subwindow = Toplevel(master=root)
    subwindow.geometry('700x527')
    """Maakt een subwindow aan voor fiets registreren."""
    background_label = Label(subwindow, image=photo2)
    background_label.place(x=0, y=0)

    label = Label(master=subwindow,text='U heeft gekozen voor: Ik wil mijn fiets registreren.', height=1, bg='#fece22')
    label.place(x=210, y=50)

    with open('fietsen.csv', 'r', newline='') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        lijst = []
        """openen van de csv fietsen.csv."""

        def registreerformulier():
                voornaam = Label(master=subwindow, text="Voornaam:", bg='#fece22')
                achternaam = Label(master=subwindow, text="Achternaam: ", bg='#fece22')
                email = Label(master=subwindow, text="Email: ", bg='#fece22')
                wachtwoord = Label(master=subwindow, text="Wachtwoord: ", bg='#fece22')
                telegramidmessage = Label(master=subwindow, text="Vul hieronder uw telegram ID in als u gebruik wilt maken van two factor authentication.", bg='#fece22')
                telegramid = Label(master=subwindow, text="Telegram ID: ", bg='#fece22')
                """Label met tekst voor entry window."""
                voornaam_entry = Entry(master=subwindow)
                achternaam_entry = Entry(master=subwindow)
                email_entry = Entry(master=subwindow)
                wachtwoord_entry = Entry(master=subwindow, show="*")
                telegramid_entry = Entry(master=subwindow)
                """Entry voor de variables."""
                voornaam.place(x=200, y=80)
                achternaam.place(x=200, y=110)
                email.place(x=200, y=140)
                wachtwoord.place(x=200, y=170)
                telegramidmessage.place(x=200, y=200)
                telegramid.place(x=200, y=230)
                """locatie van de tekst."""
                voornaam_entry.place(x=280, y=80)
                achternaam_entry.place(x=280, y=110)
                email_entry.place(x=280, y=140)
                wachtwoord_entry.place(x=280, y=170)
                telegramid_entry.place(x=280, y=230)
                """locatie van de entry voor de variables."""
                def checkregistratie():
                    """Functie checkregistratie."""
                    if str(voornaam_entry.get()) == "" or str(achternaam_entry.get()) == "":
                        naamcorrect = Label(master=subwindow, text='Vul een voornaam en achternaam in!', height=2, bg='#fece22')
                        naamcorrect.place(x=200, y=300)
                    if str('@') not in str(email_entry.get()) or str('.') not in str(email_entry.get()) or len(str(email_entry.get())) < 6 or len(str(email_entry.get())) > 30:
                        emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2, bg='#fece22')
                        emailcorrect.place(x=200, y=300)
                    """Controleerd zit er een @ in email_entry, zit er een . in email_entry, en is email_entry lang genoeg."""
                    if len(str(wachtwoord_entry.get())) < 8 or len(str(wachtwoord_entry.get())) > 12:
                        wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2, bg='#fece22')
                        wachtwoordcorrect.place(x=200, y=300)
                        """Controleerd of wachtwoord_entry lang genoeg is."""
                    elif str(voornaam_entry.get()) != "" and str(achternaam_entry.get()) != "" and str('@') in str(email_entry.get()) and str('.') in str(email_entry.get()) and len(str(email_entry.get())) >= 6 and len(str(email_entry.get())) <= 30 and len(str(wachtwoord_entry.get())) >= 8 and len(str(wachtwoord_entry.get())) <= 12:
                        with open('fietsen.csv', 'a', newline='') as schrijven:
                            stickercode = randint(10000, 99999)
                            stickercode2 = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode), bg='#fece22')
                            """geeft stickercode een random waarde tussen 10000-99999."""
                            stickercode2.place(x=300, y=300)
                            """Geeft stickercode weer."""
                            writer = csv.writer(schrijven, delimiter=';')
                            writer.writerow((str(stickercode), str(voornaam_entry.get()), str(achternaam_entry.get()), str(wachtwoord_entry.get()), str(email_entry.get()), str(telegramid_entry.get())))
                            del lijst[:]
                            """Write de registratie strings in een csv bestand."""
                            checkregistratieknop.config(state="disabled")

                checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie, fg='white', bg="#00246a")
                checkregistratieknop.place(x=300, y=260)
                """Registratie knop."""
        if len(lijst) < 50 and len(lijst) != None:
            """Als er minder dan 50 of geen rows zijn."""
            for row1 in reader:
                lijst.append(row1[0])
                """Maakt row"""
            if len(lijst) != 50:
                registreerformulier()
                """als lijst niet gelijk is aan 50, ga naar functie registreerformulier."""

        elif len(lijst) == None and len(lijst) < 50:
            registreerformulier()

        homeknop = Button(master=subwindow, text='Dit venster sluiten', command=subwindow.destroy, fg='white', bg="red")
        homeknop.place(x=485, y=493)

        stopknop = Button(master=subwindow, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

def fiets_stallen():
    """functie fits stallen."""
    subwindow2 = Toplevel(master=root)
    subwindow2.geometry('700x527')
    """Maakt subwindow."""
    background_label = Label(subwindow2, image=photo2)
    background_label.place(x=0, y=0)
    """Background van subwindow."""
    label = Label(master=subwindow2,text='U heeft gekozen voor: Ik wil mijn fiets stallen.',height=1, bg='#fece22')
    label.place(x=210, y=50)
    """Label met tekst."""
    stickercode = Label(master=subwindow2, text="Voer hier uw stickercode in: ", bg='#fece22')
    stickercode_entry = Entry(master=subwindow2)
    """Geeft variable stickercode_entry een input waarde"""
    stickercode.place(x=120, y=80)
    stickercode_entry.place(x=280, y=80)
    """Locatie van stickercode entry"""
    def checkstalling():
        """Functie checkstalling"""
        with open('stalling.csv', 'a', newline='') as schrijven:
            """Open stalling.csv"""
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                list = []
                for row in reader:
                        list.append(row[0])
                        """Maakt een extra row"""
                if str(stickercode_entry.get()) in list:
                        """Als stickercode entry in fietsen.csv zit"""
                        writer = csv.writer(schrijven, delimiter=';')
                        if row[0] == str(stickercode_entry.get()):
                            voornaam = row[1]
                            achternaam = row[2]
                            writer.writerow((str(stickercode_entry.get()), voornaam, achternaam, str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))))
                            """Write in het CSV bestand"""
                            label = Label(master=subwindow2,text='Uw fiets is gestald!',height=1, bg='#fece22')
                            label.place(x=120, y=140)
                            checkstallingknop.config(state="disabled")
                elif str(stickercode_entry.get()) not in list:
                    """als stickercode niet in fietsen.csv zit print(x)"""
                    nietindatabase = Label(master=subwindow2,text='Deze stickercode komt niet overeen met de database!',height=1, bg='#fece22')
                    nietindatabase.place(x=120, y=140)

    checkstallingknop = Button(master=subwindow2, text='Stal fiets', command=checkstalling, fg='white', bg="#00246a")
    checkstallingknop.place(x=310, y=110)

    homeknop = Button(master=subwindow2, text='Dit venster sluiten', command=subwindow2.destroy, fg='white', bg="red")
    homeknop.place(x=485, y=493)

    stopknop = Button(master=subwindow2, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
    stopknop.place(x=600, y=493)
    """Button+locatie"""

def fiets_ophalen():
    """Functie fiets ophalen"""
    subwindow3 = Toplevel(master=root)
    subwindow3.geometry('700x527')
    """Maakt subwindow"""
    background_label = Label(subwindow3, image=photo2)
    background_label.place(x=0, y=0)
    """Maakt background voor subwindow"""
    label = Label(master=subwindow3,text='U heeft gekozen voor: Ik wil mijn fiets ophalen.',height=1, bg='#fece22')
    label.place(x=210, y=50)
    """Maakt label met tekst"""
    stickercode = Label(master=subwindow3, text="Voer hier uw stickercode in: ", bg='#fece22')
    stickercode_entry = Entry(master=subwindow3)
    wachtwoord = Label(master=subwindow3, text="Voer hier uw wachtwoord in: ", bg='#fece22')
    wachtwoord_entry = Entry(master=subwindow3, show="*")
    """Maakt labels met tekst + entry"""
    stickercode.place(x=120, y=80)
    stickercode_entry.place(x=280, y=80)
    wachtwoord.place(x=120, y=110)
    wachtwoord_entry.place(x=280, y=110)
    """Geeft locatie aan label en grid"""
    with open('fietsen.csv', 'r') as lezen:
        reader = csv.reader(lezen, delimiter=';')
        list = []
        for row in reader:
            list.append(row[0])

        def checkophalen():
            """Functie checkophlaen"""
            if str(stickercode_entry.get()) not in list:
                nietindatabase = Label(master=subwindow3,text='Deze stickercode komt niet overeen met de database!',height=1, bg='#fece22')
                nietindatabase.place(x=120, y=170)
                """Als stickercode niet in list staan print(x)"""
            elif str(stickercode_entry.get()) in list:
                with open('fietsen.csv', 'r') as lezen:
                    reader = csv.reader(lezen, delimiter=';')
                    incorrectWachtwoord = 0
                    for row in reader:
                        if row[0] == str(stickercode_entry.get()) and row[3] == str(wachtwoord_entry.get()):
                            """Als de ingevoerde stickercode en wachtwoord overeenkomen met row[0] en row[3] print(x)"""
                            kluisopen = Label(master=subwindow3,text='Uw fietsenkluis is open!',height=1, bg='#fece22')
                            kluisopen.place(x=120, y=170)
                            regel_verwijderen(str(stickercode_entry.get()))
                            """Verwijdert je line uit stalling.csv"""
                            telegramid = row[5]
                            if telegramid != '':
                                link = 'https://api.telegram.org/bot275900175:AAG2uOgInzsASLcorHUaZgMAGvvklfAIGUk/sendmessage?chat_id=' + str(telegramid) + '&text=Uw%20fiets%20is%20opgehaald%20vanaf%20de%20stalling,%20was%20u%20dit%20niet?%20bel%20dan%20snel%20naar%20onze%20helpdesk:%200900-0123456'
                                webbrowser.open(link)
                                """stuurt je een bericht via telegram als je fiets is opgehaalt"""
                        else:
                            incorrectWachtwoord += 1
                    if incorrectWachtwoord == len(row):
                        incorrectpassword = Label(master=subwindow3,text='Incorrect wachtwoord!',height=1, bg='#fece22')
                        incorrectpassword.place(x=120, y=170)
                        """Als het wachtwoord niet klopt print(x)"""

        checkophalenknop = Button(master=subwindow3, text='Haal fiets op', command=checkophalen, fg='white', bg="#00246a")
        checkophalenknop.place(x=300, y=140)
        """Knoppen om fiets ophalen af te ronden"""
        homeknop = Button(master=subwindow3, text='Dit venster sluiten', command=subwindow3.destroy, fg='white', bg="red")
        homeknop.place(x=485, y=493)

        stopknop = Button(master=subwindow3, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

def regel_verwijderen(stickercode):
    """Functie regel_verwijderen."""
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
                """maakt nieuwe row voor stickercodes, voornamen, achternamen en data"""

    with open('stalling.csv', 'w', newline='') as schrijven:
        writer = csv.writer(schrijven, delimiter=';')
        i = 0
        while i < len(stickercodes):
            writer.writerow((stickercodes[i] , voornamen[i], achternamen[i], datums[i]))
            i = i + 1
            """Verwijdert één rij uit de stalling.csv."""

def informatie_opvragen():
    """Functie informatie_opvragen"""
    subwindow4 = Toplevel(master=root)
    subwindow4.geometry('700x527')
    """Maakt een subwindow"""
    background_label = Label(subwindow4, image=photo2)
    background_label.place(x=0, y=0)
    """Geeft subwindow een background"""
    label = Label(master=subwindow4,text='U heeft gekozen voor: Ik wil informatie opvragen.',height=1, bg='#fece22')
    label.place(x=210, y=50)
    """Print een stuk tekst in de subwindow"""

    def informatie_keuze_1():
        """Functie informatie_keuze__1"""
        subwindow5 = Toplevel(master=root)
        subwindow5.geometry('700x527')
        """Maakt subwindow"""
        background_label = Label(subwindow5, image=photo2)
        background_label.place(x=0, y=0)
        """Geeft subwindow een background"""
        with open('stalling.csv', 'r', newline='') as lezen:
            reader = csv.reader(lezen, delimiter=';')
            lijst = []
            for row1 in reader:
                lijst.append(row1[0])
            stalplaatsenbezet = len(lijst)
            stalplaatsenbeschikbaar = 50 - stalplaatsenbezet
            """Berekent hoeveel plaatsen er nog beschikbaar zijn"""
            if stalplaatsenbeschikbaar >= 1:
                stalplaatsen = Label(master=subwindow5,text='Er zijn nog ' + str(stalplaatsenbeschikbaar) + ' stalplaatsen beschikbaar.',height=1, bg='#fece22')
                stalplaatsen.place(x=210, y=50)
                """Als er 1 of meer plaatsen beschikbaar zijn print(x)"""
            if stalplaatsenbeschikbaar == 0:
                vol = Label(master=subwindow5,text='Alle stalplaatsen zijn momenteel bezet, probeer het later opnieuw.',height=1, bg='#fece22')
                vol.place(x=210, y=50)
                """Als er 0 plaatsen beschikbaar zijn print(x)"""

        homeknop = Button(master=subwindow5, text='Dit venster sluiten', command=subwindow5.destroy, fg='white', bg="red")
        homeknop.place(x=485, y=493)

        stopknop = Button(master=subwindow5, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

    def informatie_keuze_2():
        """Functie Informatie_keuze_2"""

        subwindow6 = Toplevel(master=root)
        subwindow6.geometry('700x527')
        """Maakt subwindow"""
        background_label = Label(subwindow6, image=photo2)
        background_label.place(x=0, y=0)
        """Maakt background"""
        kosten = Label(master=subwindow6,text='De 1e dag is gratis, daarna betaal je 50 cent per dag.',height=1, bg='#fece22')
        kosten.place(x=210, y=50)
        """Maakt label met tekst"""
        homeknop = Button(master=subwindow6, text='Dit venster sluiten', command=subwindow6.destroy, fg='white', bg="red")
        homeknop.place(x=485, y=493)

        stopknop = Button(master=subwindow6, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)

    def informatie_keuze_3():
        """Functie informatie_keuze_3"""
        subwindow7 = Toplevel(master=root)
        subwindow7.geometry('700x527')
        """Maakt subwindow"""
        background_label = Label(subwindow7, image=photo2)
        background_label.place(x=0, y=0)
        """Maakt background"""
        stickercode = Label(master=subwindow7, text="Voer hier uw stickercode in: ", bg='#fece22')
        stickercode_entry = Entry(master=subwindow7)
        email = Label(master=subwindow7, text="Voer hier uw email in: ", bg='#fece22')
        email_entry = Entry(master=subwindow7)
        """Input voor email en sticckercode om wachtwoord op te halen"""
        stickercode.place(x=140, y=80)
        stickercode_entry.place(x=300, y=80)
        email.place(x=140, y=110)
        email_entry.place(x=300, y=110)
        """Locatie van input voor email en stickercode"""
        def checkwachtwoord():
            """Functie Checkwachtwoord"""
            with open('fietsen.csv', 'r') as lezen:
                reader = csv.reader(lezen, delimiter=';')
                email_onbekend = 0
                stickercode_onbekend = 0
                rows = 0
                """Geeft waarde 0 aan 3 variables"""
                for row in reader:
                    rows += 1
                    """Maakt extra row"""
                    if str(email_entry.get()) == row[4] and str(stickercode_entry.get()) == row[0]:
                        wachtwoord = Label(master=subwindow7, text="Uw wachtwoord is: " + row[3], bg='#fece22')
                        wachtwoord.place(x=140, y=170)
                        """Als stickercode en email input kloppen, print(x)"""
                        telegramid = row[5]
                        if telegramid != '':
                            link = 'https://api.telegram.org/bot275900175:AAG2uOgInzsASLcorHUaZgMAGvvklfAIGUk/sendmessage?chat_id=' + str(telegramid) + '&text=Uw%20wachtwoord%20is%20opgehaald%20via%20de%20wachtwoord%20vergeten%20functie%20,%20%20was%20u%20dit%20niet?%20bel%20dan%20snel%20naar%20onze%20helpdesk:%200900-0123456'
                            webbrowser.open(link)
                            """Stuur bericht via telegram app als je wachtwoord wordt opgevraagt"""
                    if str(email_entry.get()) != row[4]:
                        email_onbekend += 1
                        """Als email entry niet klopt, geef variable +1"""
                    if str(stickercode_entry.get()) != row[0]:
                        stickercode_onbekend += 1
                        """Als stickercode entry niet klopt, geef variable +1"""
                if email_onbekend == rows:
                    email = Label(master=subwindow7, text="Het Email adres komt niet overeen met de database!", bg='#fece22')
                    email.place(x=140, y=140)
                    """Als email_onbekend niet bestaat, print(x)"""
                if stickercode_onbekend == rows:
                    stickercode = Label(master=subwindow7, text="De stickercode komt niet overeen met de database!", bg='#fece22')
                    stickercode.place(x=140, y=140)
                    """Als stickercode niet bestaat, print(x)"""

        wachtwoordknop = Button(master=subwindow7, text='Vraag mijn wachtwoord op', command=checkwachtwoord, fg='white', bg="#00246a")
        wachtwoordknop.place(x=270, y=140)
        """Knop om wachtwoord op te vragen"""
        homeknop = Button(master=subwindow7, text='Dit venster sluiten', command=subwindow7.destroy, fg='white', bg="red")
        homeknop.place(x=485, y=493)

        stopknop = Button(master=subwindow7, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
        stopknop.place(x=600, y=493)


    keuze1knop = Button(master=subwindow4, text='Ik wil weten hoeveel stalplaatsen nog vrij zijn.', command=informatie_keuze_1, fg='white', bg="#00246a")
    keuze1knop.place(x=230, y=80)
    """Informatieknop_1"""
    keuze2knop = Button(master=subwindow4, text='Ik wil weten wat de kosten zijn.', command=informatie_keuze_2, fg='white', bg="#00246a")
    keuze2knop.place(x=260, y=120)
    """Informatieknop_2"""
    keuze3knop = Button(master=subwindow4, text='Ik ben mijn wachtwoord vergeten.', command=informatie_keuze_3, fg='white', bg="#00246a")
    keuze3knop.place(x=250, y=160)
    """Informatieknop_3"""
    homeknop = Button(master=subwindow4, text='Dit venster sluiten', command=subwindow4.destroy, fg='white', bg="red")
    homeknop.place(x=485, y=493)

    stopknop = Button(master=subwindow4, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
    stopknop.place(x=600, y=493)

def stoppen():
    """Functie stoppen"""
    exit()
    """Exit applicatie"""


registreerknop = Button(master=root, text='Ik wil mijn fiets registreren', command=fiets_registreren, fg='white', bg="#00246a")
registreerknop.place(x=50, y=350)
"""Registreerknop voor functie Fiets_Registreren"""
stalknop = Button(master=root, text='Ik wil mijn fiets stallen', command=fiets_stallen, fg='white', bg="#00246a")
stalknop.place(x=210, y=350)
"""Stalknop voor functie fiets_Stallen"""
ophaalknop = Button(master=root, text='Ik wil mijn fiets ophalen', command=fiets_ophalen, fg='white', bg="#00246a")
ophaalknop.place(x=350, y=350)
"""Ophaalknop voor functie Fiets_ophalen"""
informatieopvragenknop = Button(master=root, text='Ik wil informatie opvragen', command=informatie_opvragen, fg='white', bg="#00246a")
informatieopvragenknop.place(x=500, y=350)
"""Informatievragenknop voor functie Informatie_Opvragen"""
stopknop = Button(master=root, text='Ik wil stoppen', command=stoppen, fg='white', bg="red")
stopknop.place(x=600, y=493)
"""stopknop voor functie Stoppen"""

root.iconbitmap('favicon.ico')
root.geometry('700x527')
root.mainloop()
"""Maakt main window aan"""
