# Ohjelman arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on jaettu siten, että pakkaus *user_interface* sisältää 
käyttöliittymään liittyvän koodin ja pakkaus *application_logic* sisältää
kaikki sovelluslogiikkaan liittyvän koodin.

![Pakkausrakenne](/dokumentaatio/kuvat/pakkaukset.jpg)

## Käyttöliittymä

Ohjelman käyttöliitymässä on vain yksinäkymä, joka on itse pelinäkymä. 

[Level](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/application_logic/level.py)-luokka 
vastaa kaikesta pelaamiseen liityvistä elemneteistä, kuten pisteistä ja pelin tilasta 
(eli onko peli hävitty, voitettu vai vielä kesken) sekä siitä, monesko taso on meneillään. 
Pelinäkymän näyttämisestä vastaa [Renderer](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/user_interface/renderer.py)-luokka.

Pelaajan syötteitä luetaan [Gameloop](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/application_logic/gameloop.py)-luokan avulla, 
jossa syötteet käsitellään ja tehdään syötteen mukaiset muutokset pelinäkymään.

## Sovelluslogiikka

Sovelluslogiikan (ja käyttöliittymän) luokkakaavio näyttää seuraavalta:

![Luokkakaavio, jossa on kaikki yhteydet](/dokumentaatio/kuvat/luokkakaavio.png)

## Päätoiminnallisuudet

Pelin tärkeimpiin toiminnallisuuksiin kuuluu neliöiden kääntäminen klikkaamalla ja uuden tason luominen pelin
päätyttyä game overiin tai tason läpäisemiseen.

### Neliön kääntäminen

Kun jotakin kääntämätöntä neliötä klikataan, etenee pelin kontrolli seuraavasti:

![Neliön kääntäminen](/dokumentaatio/kuvat/flipping.png)

Kun neliötä klikataan, Gameloopin eventseihin tulee uusi tapahtuma, joka käsitellää event_handling()-funktio avulla.

### Muut toiminnallisuudet

Uudelle tasolle siirtyminen noudattaa samaa kaavaa kuin neliön kääntäminen siihen asti, kun selvitetään tason game_over-atribuutin 
tilanne ja kuinka paljon pistetitä on kertynyt. Jos game_over on True, luomme uuden tason siinä kohtaa. 
Jos game_over on False ja tason pisteet vastaavat maksimipisteitä, luomme uuden tason siinä kohtaa. 

