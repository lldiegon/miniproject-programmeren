# miniproject-programmeren

README van NS-fietsenstalling.py

Gemaakt door:
Diego Nijboer
Jan de Waal
Ruben Verstappen
Maarten de Leeuw
Daniël Reus


Inhoud:

1. Introductie
2. De bestanden
3. Telegrambot
4. De applicatie
5. Screencast
6. Einde

1. Introductie

Deze applicatie is gemaakt voor een fietsenstalling. Hiermee kan een fiets worden geregistreerd, vervolgens worden gestald en later worden opgehaald. 
Er zit ook een informatie opvraag optie bij om het programma gebruiksvriendelijk te maken. Daarnaast zijn er een aantal bestand nodig zodat de applicatie goed werkt.

De Telegram bot werkt alleen als een gebruiker een berichtje stuurt via de bot. We hebben de applicatie zo gemaakt dat als de gebruiker hier geen van gebruikt wil maken of geen Telegram
heeft, dat de applicatie nog steeds werkt. Zodra iemand hier gebruik van heeft gemaakt, kan hij later niet meer het programma gebruiken zonder de Telegram identification, anders zou
de beveiliging geen nut hebben.

2. De bestanden

Er zijn een aantal bestanden die gedownload moeten worden voor dat de applicatie gestart kan worden. Ze staan in ook in "resources". 
De volgende bestanden moeten in dezelfde directory staan als de applicatie:
- Background_fietsenstalling.png
- Background_other.png
- favicon.ico

3. Telegrambot

De Telegrambot linkt een gebruiker aan een account. De Telegrambot kan zien welk ID iemand heeft op Telegram. Vervolgens kan hij met deze ID een bericht versturen. 
Zodra iemand een fiets ophaalt die gekoppeld is aan een Telegram ID, ontvangt deze gebruiker een bericht dat zijn fiets is opgehaald. 
Als een gebruiker zijn Telegram ID wel heeft geregistreerd, maar bij het ophalen is vergeten, dan kan deze zijn fiets niet ophalen. 

Via onderstaande link die je opent in een webbrowser, kan je een bericht sturen naar de Telegrambot. Vervolgens kan de Telegrambot zijn wat jouw ID is. 

https://telegram.me/FietsenStallingbot

In onderstaande link kan je je ID achterhalen. 

https://api.telegram.org/bot275900175:AAG2uOgInzsASLcorHUaZgMAGvvklfAIGUk/getupdates

""message":{"message_id":455,"from":{"id":245826695,"first_name":"Dani\u00ebl"},"chat":{"id":245826695,"first_name":"Dani\u00ebl","type":"private"},"date":1478253789,"text":"\/start","entities":
[{"type":"bot_command","offset":0,"length":6}]}}]}"

Bovenstaande is het laatste bericht dat gestuurd is naar de bot. Je kan zien dat er een message_id is en een "id". Het gaat om dit laatste ID is.

Als de ID wordt gebruikt bij het registeren, dan zal de bot een bericht sturen naar dit ID. Je kan natuurlijk net alsof doen of je een Telegram ID hebt, maar dan krijg je geen berichtje.

4. De applicatie

De applicatie wordt gestart door op het bestand "miniprojectgroep2.py" te klikken. Python wordt vervolgens opgestart en vervolgens krijg je het GUI te zien.

Er zijn 4 opties die gekozen kunnen worden en daarnaast een extra "ik wil stoppen knop" die de applicatie afsluiten.

De 4 opties zijn:

- Registreren
- Stallen
- Ophalen
- Informatie ophalen

Registreren: 
Hiermee kan je je fiets opslaan in het bestand fietsen.csv. Het bestand herkent dan de gebruiker en de stickercode die aan de fiets wordt gekoppeld. Hier kan ook gekozen worden om 
van de Telegrambot gebruik te maken, maar dat is niet verplicht.

Stallen:
Het stallen van de fiets plaats de fiets in de fietsenstalling. Dit kan alleen gedaan worden door gebruikers die geregistreerd zijn. De fietsenstalling zelf heeft maar 50 plekken, maar er 
zijn natuurlijk veel meer gebruikers mogelijk. Niet iedereen houdt zijn fiets altijd in de stalling, dus moeten er meer gebruikers kunnen zijn dan fietsen die in de stalling staan.

Ophalen:
Hiermee wordt de fiets opgehaald en verwijdert uit stalling.csv. De registratie blijft wel bestaan in fietsen.csv. Als er gebruik gemaakt is van de Telegrambot, moet er ook een TelegramID
worden ingevoerd. Zo niet, dan blijft de fiets in de stalling staan. De Telegrambot stuurt een berichtje naar de gebruiker als de fiets wordt opgehaald. 

Informatie ophalen:
Deze functie geeft nog een aantal opties.

- Ik wil weten hoeveel stalplaatsen nog vrij zijn
- Ik wil weten wat de kosten zijn
- Ik ben mijn wachtwoord vergeten

De eerste optie geeft aan hoeveel stalplaatsen nog in stalling.csv beschikbaar zijn. De 2e optie geeft een korte omschrijving wat de kosten zijn, maar die zijn buiten beschouwing gelaten 
voor dit project.

Het wachtwoord ophalen leest wat iemands wachtwoord is op basis van iemands email en stickercode. Aangezien de stickercode alleen op de fiets staat, kan niemand zomaar het wachtwoord 
achterhalen. Als je de fiets zou willen stelen, zou je de fiets al moeten hebben. Dan heb je de fiets al gestolen en maakt de beveiliging hierop ook niet uit. Je zou de stalling ook niet 
in kunnen lopen zonder dat je de optie "fiets ophalen" hebt doorlopen.

5. Screencast

Voor verdere uitleg over de code kan de screencast bekeken worden waar de code wordt uitgevoerd. Zie het bestand "Screencast team 2" hiervoor.

6. Einde

Dit was het einde van de README. 



