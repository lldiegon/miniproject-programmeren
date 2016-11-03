from tkinter import *
import csv
from random import randint
from datetime import datetime

root = Tk()
label = Label(master=root, text='Kies een van de onderstaande opties!', height=2)
label.pack()

photo = PhotoImage(file="das fiets.png")
background_label = Label(root, image=photo)
background_label.pack()
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def fiets_registreren():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    subwindow.geometry('575x390')

    background_label = Label(subwindow, image=photo)
    background_label.pack()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = Label(master=subwindow,text='U heeft gekozen voor: Ik wil mijn fiets registreren.',height=2)
    label.pack()

    entry = Entry(master=root)
    entry.pack(padx=10, pady=10)

    with open('fietsen.csv', 'r', newline='') as lezen:
        with open('fietsen.csv', 'a', newline='') as schrijven:
            reader = csv.reader(lezen, delimiter=';')
            lijst = []
            if len(lijst) < 50 and len(lijst) != None:

                for row1 in reader:
                    lijst.append(row1[0])

                if len(lijst) != 50:
                    stickercode = randint(10000, 99999)

                    writer = csv.writer(schrijven, delimiter=';')
                    voornaam = Label(master=subwindow, text="Voornaam")
                    achternaam = Label(master=subwindow, text="Achternaam")
                    email = Label(master=subwindow, text="Email")
                    wachtwoord = Label(master=subwindow, text="wachtwoord")
                    stickercode = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode))

                    voornaam_entry = Entry(master=subwindow)
                    achternaam_entry = Entry(master=subwindow)
                    email_entry = Entry(master=subwindow)
                    wachtwoord_entry = Entry(master=subwindow, show="*")

                    voornaam.grid(row=0, sticky=E)
                    achternaam.grid(row=1, sticky=E)
                    email.grid(row=2, sticky=E)
                    wachtwoord.grid(row=3, sticky=E)

                    voornaam_entry.grid(row=0, column=1)
                    achternaam_entry.grid(row=1, column=1)
                    email_entry.grid(row=2, column=1)
                    wachtwoord_entry.grid(row=3, column=1)



                    def checkregistratie():
                        if str('@') not in email_entry or str('.') not in email_entry or len(email_entry) < 6 or len(email_entry) > 30:
                            emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2)
                            emailcorrect.grid(row=2, column=2)

                        if len(wachtwoord_entry) < 8 or len(wachtwoord_entry) > 12:
                            wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2)
                            wachtwoordcorrect.grid(row=3, column=2)
                        else:
                            writer.writerow((stickercode, voornaam_entry, achternaam_entry, wachtwoord_entry, email_entry))
                            del lijst[:]

                    checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie())
                    checkregistratieknop.grid(row=4, column=1)

                else:
                    vol = Label(master=subwindow, text='Alle stalplaatsen zijn momenteel in gebruik, probeer het later opnieuw.')
                    vol.grid(row=4, column=2)

            elif len(lijst) == None and len(lijst) < 50:
                stickercode = randint(10000, 99999)

                writer = csv.writer(schrijven, delimiter=';')
                voornaam = Label(master=subwindow, text="Voornaam")
                achternaam = Label(master=subwindow, text="Achternaam")
                email = Label(master=subwindow, text="Email")
                wachtwoord = Label(master=subwindow, text="wachtwoord")
                stickercode = Label(master=subwindow, text="Uw unieke sticker code is: " + str(stickercode))

                voornaam_entry = Entry(master=subwindow)
                achternaam_entry = Entry(master=subwindow)
                email_entry = Entry(master=subwindow)
                wachtwoord_entry = Entry(master=subwindow, show="*")

                voornaam.grid(row=0, sticky=E)
                achternaam.grid(row=1, sticky=E)
                email.grid(row=2, sticky=E)
                wachtwoord.grid(row=3, sticky=E)

                voornaam_entry.grid(row=0, column=1)
                achternaam_entry.grid(row=1, column=1)
                email_entry.grid(row=2, column=1)
                wachtwoord_entry.grid(row=3, column=1)



                def checkregistratie():
                    if str('@') not in email_entry or str('.') not in email_entry or len(email_entry) < 6 or len(email_entry) > 30:
                        emailcorrect = Label(master=subwindow, text='Dit email adres is niet geldig!', height=2)
                        emailcorrect.grid(row=2, column=2)

                    if len(wachtwoord_entry) < 8 or len(wachtwoord_entry) > 12:
                        wachtwoordcorrect = Label(master=subwindow, text='Het gekozen wachtwoord moet minimaal 8 letters lang zijn en maximaal 12 letters lang!', height=2)
                        wachtwoordcorrect.grid(row=3, column=2)
                    else:
                        writer.writerow((stickercode, voornaam_entry, achternaam_entry, wachtwoord_entry, email_entry))
                        del lijst[:]

                checkregistratieknop = Button(master=subwindow, text='Registreren', command=checkregistratie())
                checkregistratieknop.grid(row=4, column=1)





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
