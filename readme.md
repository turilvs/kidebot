# KideBot

Ohjelmistorobotti, johon rakennettu pieni käyttöliittymä. Käyttöliittymän avulla ostetaan automaattisesti maksimimäärä haluttuja lippuja Kide.appista.
Käyttää Google Chromea ja chromedriveria.
Automatisointi toteutettu Seleniumilla.

## Alustus
<img width="403" alt="kidebotEtusivu" src="https://github.com/turilvs/kidebot/assets/97661374/f398dcb8-71e3-4559-b6c2-199f0b67427b">

Alustuksessa botti alustetaan, jolloin Google Chrome-ikkuna aukeaa, ja ohjelmistorobotti voi ohjata kyseistä ikkunaa.
Kun botti on alustettu, voidaan käyttöliittymän avulla liikkua Kide.appin sivuilla joko etusivulle, tai rajata lippuja ilmaisten, suosikkien tai myöhemmin myyntiin tulevien lippujen välillä.

## Osto
<img width="401" alt="kidebotOsto" src="https://github.com/turilvs/kidebot/assets/97661374/3eac0970-2b1d-478e-85d5-d531929bdef7">

Kun ollaan siirrytty haluttujen lippujen sivulle, ostaa botti nappia painamalla maksimimäärän saatavilla olevia lippuja.
Jos liput ovat vasta tulossa myyntiin, botti alkaa päivittää sivua jatkuvasti, ja ostaa maksimimäärän saatavilla olevia lippuja heti mahdollisuuden tultaessa.
