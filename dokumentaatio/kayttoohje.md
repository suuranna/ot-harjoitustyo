# Käyttöohje

Lataa pelin lähdekoodi tuoreimmasta releasesta.

## Ohjelman käynnistäminen

Jotta ohjelma toimisi, asennetaan ensin riippuvuudet komennolla

`poetry install`

Nyt ohjelman voi käynnistää komennolla

`poetry run invoke start`


## Pelin aloittaminen

Ohjelman käynnistäminen antaa seuraavan näkymän:

![Pelin aloittaminen](/kuvat/begining.png)

## Neliön kääntäminen

Kun neliötä klikkaa, näkymä muuttuu klikatun neliön osalta seuraavasti:

![Neliön klikkaaminen](/kuvat/flip.png)

## Tason läpäisy

Kun omat pisteet saavuttavat maksimipisteet eli kaikki kakkoset ja kolmoset on löydetty,
muuttuu näkymä seuraavasti:

![Tason läpäiseminen](/kuvat/level_completed.png)

Kun pelinäkymää klikkaa mistä kohtaa vain, pelinäkymään tulee uusi taso.

## Game over

Peli loppuu, jos klikkaa sellaista neliötä, jonka "kääntöpuolella" on pommi, jolloin pelinäkymä
näyttää seuraavalta:

![Game over](/kuvat/game_over.png)

Kun pelinäkymää klikkaa mistä kohtaa vain, pelinäkymään tulee taso 1.

