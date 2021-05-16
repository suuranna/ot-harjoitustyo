# Ohjelmistotekniikka, harjoitustyö
## Miinaharavan ja picrossin risteymä -peli

Pelissä on 5x5 kokoinen ruudukko neliöitä, joita kääntämällä/klikkaamalla kortin alta 
paljastuu joku luku väliltä 1-3 tai pommi. Pelin tavoitteena on löytää kaikki luvut 2 ja 3
ja välttää kääntämästä neliöitä, joissa on pommi. Peli loppuu, jos kääntää kortin, jossa 
on pommi. Tarkemmat ohjeet määrittelydokumentissa sekä käyttöohjeissa. 

## Linkki releaseen

[Linkki viikon 5 releaseen](https://github.com/suuranna/ot-harjoitustyo/releases/tag/viikko5)

[Linkki viikon 6 releaseen](https://github.com/suuranna/ot-harjoitustyo/releases/tag/viikko6)

[Valmiin sovelluksen release]()

## Dokumentaatio

[Harjoitustyön työaikakirjainpito](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Harjoitustyön määrittelydokumentti](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/maarittelydokumentti.md)

[Harjoitustyön arkkitehtuuri](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Harjoitustyön käyttöohje](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Harjoitustyön testausdokumentti](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Komentorivitoiminnot

### Asennus

Ohjelman saa toimimaan asentamalla ensin riippuvuudet komennolla:

`poetry install`

### Ohjelman suorittaminen

Ohjelma käynnistyy komennolla

`poetry run invoke start`


### Testaaminen ja testikattavuus

Testit voi suorittaa komennolla

`poetry run invoke test`

Ja testikattavuusraportin saa generoitua htmlcov-hakemiston index-html-tiedostoon komennolla

`poetry run invoke coverage-report`

### Koodin laadun tarkastamine Pylintillä

Koodin laadun, eli miten hyvin .pylintrc-tiedoston vaatimukset toteutuvat koodissa, voi tarkastaa komennolla

`poetry run invoke lint`


