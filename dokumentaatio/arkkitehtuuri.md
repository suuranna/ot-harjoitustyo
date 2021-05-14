# Ohjelman arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on jaettu siten, että pakkaus *user_interface* sisältää 
käyttöliittymään liittyvän koodin ja pakkaus *application_logic* sisältää
kaikki sovelluslogiikkaan liittyvän koodin.

## Käyttöliittymä

Ohjelman käyttöliitymässä on vain yksinäkymä, joka on itse pelinäkymä. 

[Level](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/application_logic/level.py)-luokka 
vastaa kaikesta pelaamiseen liityvistä elemneteistä, kuten pisteistä ja pelin tilasta 
(eli onko peli hävitty, voitettu vai vielä kesken) sekä siitä, monesko taso on meneillään. 
Pelinäkymän näyttämisestä vastaa [Renderer](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/user_interface/renderer.py)-luokka.

Pelaajan syötteitä luetaan [Gameloop](https://github.com/suuranna/ot-harjoitustyo/blob/master/src/application_logic/gameloop.py)-luokan avulla, jossa syötteet käsitellään ja tehdään syötteen mukaiset muutokset pelinäkymään.

## Sovelluslogiikka

-

## Päätoiminnallisuudet

-
