# Testausdokumentti

Ohjelman testaamista varten on tehty testejä, jotka hyödyntävät unittestiä. 

# Sovelluslogiikka

Testit kattavat vain application_logic-kansiossa olevat tiedostot ja niiden koodin enemmän tai vähemmän.
Näin ollen vain sovelluslogiikkaa testataan. Jokaista sovelluslogiikan tiedostoa vastaa oma testitiedosto tests-kansiossa.  

## Testikattavuusraportti
 
Kayttöliittyymään liittyvän koodin testien haarautumakattavuus on 65%

![Coverage report](/dokumentaatio/kuvat/coverage_report.png)

Testauksen ulkopuolelle jäi suurinosa gameloopia ja generate_matrix-metodi.
