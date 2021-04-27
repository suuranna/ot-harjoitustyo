# Ohjelmistotekniikka, harjoitustyö
## Miinaharavan ja picrossin risteymä -peli

Pelissä on 5x5 kokoinen ruudukko "kortteja", joita kääntämällä/klikkaamalla kortin alta 
paljastuu joku luku väliltä 1-3 tai pommi. Pelin tavoitteena on löytää kaikki luvut 2 ja 3
ja välttää kääntämästä kortteja, joissa on pommi. Peli loppuu, jos kääntää kortin, jossa 
on pommi. Tarkemmat ohjeet määrittelydokumentissa. 

## Linkki releaseen

[]yaas

## Dokumentaatio

[Harjoitustyön työaikakirjainpito](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Harjoitustyön määrittelydokumentti](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/maarittelydokumentti.md)

[Harjoitustyön arkkitehtuuri](https://github.com/suuranna/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

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


