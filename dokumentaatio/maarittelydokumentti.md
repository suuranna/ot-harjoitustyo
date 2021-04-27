# Määrittelydokumentaatio pelistä
## Sovelluksen tarkoitus
Toteutan sovelluksena pelin, joka on Picrossin ja Miinaharavan risteytys, ja jossa on sama idea, 
kuin Nintendon Pokemon HeartGold & SoulSilver peleissä esiintyvässä minipelissä nimeltään Voltorb Flip. 
Pelissä on 5x5 ruudukko, jossa on pommeja ja lukuja 1, 2 ja 3. Jokaisen rivin ja sarakkeen 
kohdalla kerrotaan kuinka monta pommia kyseisellä rivillä/sarakkeella on 
ja mikä on siinä olevien lukujen summa. (Esim. jos rivillä on 1, pommi, pommi, 3 ja 2, 
kerrottaisiin pommeja olevan 2 ja summan olevan 6). Pelin ideana on löytää 
ruudukosta kaikki kakkoset ja kolmoset. 

## Käyttäjät
Pelissä on vain yhdenlaisia käyttäjiä

## Suunnitellut toiminnallisuudet
* Aloitusnäkymä, josta pääsee aloittamaan pelin tasolta 1
* Pelinäkymässä on 5x5 ruudukko, jossa kaikki ruudut näyttävät aluksi samalta (tehty viikolle 4)
* Pelinäkymän ruutujen numerot ja pommit ovat joka kerralla eri, eli ne randomoidaan. **(tehty viikolle 5)**
* Jokaisen rivin vasemmalla puolella ja sarakkeen yläpuolella näkyy sen rivin/sarakkeen 
lukujen summa. (tehty viikolle 4)
* Jokaisen rivin vasemmalla puolella ja sarakkeen yläpuolella näkyy kyseisen rivin/sarakkeen 
pommien määrä. **(tehty viikolle 5)** 
* Pelin edetessä ruutua klikkaamalla paljastuu, onko ruudussa pommi vai luku. **(tehty viikolle 5)**
* Yläkulmassa näkyy pisteet. (tehty viikolle 4)
* Pisteet kasvavat siten, että ruudussa olevalla luvulla kerrotaan sen hetkiset pisteet (eli ykkösen 
löytäessä ei tapahdu mitään, ellei kyseessä ole ensimmäinen klikkaus). Alussa kuitenkin 
aloituspisteiksi tulee ensimmäisen klikatun ruudun luku. (tehty viikolle 4)
* Jos ruudussa on pommi, peli loppuu. 
* Kun kaikki kakkoset ja kolmoset on löydetty, taso on läpäisty ja pelaaja pääsee 
etenemään seuraavalle tasolle.

 
### Perusversiota laajentavat ominaisuudet
* Kirjaitumismahdollisuus, jolloin on mahdollista pitää kirjaa siitä, kuinka monta tasoa pelaaja on läpäissyt ja kuinka monta pistettä hän on saanut 
yhteensä kerättyä.
* Jokaiselta läpäisyltä tasolta saa pisteitä, jotka lisätään omiin pisteisiin.
* Jokaisen käyttäjän pisteistä voi muodostaa scoreboardin
* Peli vaikenee sitä mukaan, kuinka monta tasoa pelaaja läpäisee peräkkäin. Vaikeus näkyy pommien määrässä ja/tai ruudukon kasvamisena. 
* Merkintänäkymä, jossa voi jokaiseen ruutuun merkitä, mitä luule siinä olevan.  
