import unittest
from  kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate = Kassapaate()
		self.rikaskortti = Maksukortti(500)
		self.koyhakortti = Maksukortti(1)

	def test_onko_kassapaate_luotu_oikein(self):
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

	def test_kateisto_toimii_edullisesti_riittava_maksu(self):
		palautettava = self.kassapaate.syo_edullisesti_kateisella(500)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
		self.assertEqual(self.kassapaate.edulliset, 1)
		self.assertEqual(palautettava, 260)

	def test_kateisto_toimii_edullisesti_ei_riittava_maksu(self):
                palautettava = self.kassapaate.syo_edullisesti_kateisella(100)
                self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
                self.assertEqual(palautettava, 100)
                self.assertEqual(self.kassapaate.edulliset, 0)


	def test_kateisto_toimii_maukkaasti_riittava_maksu(self):
		palautettava = self.kassapaate.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
		self.assertEqual(palautettava, 100)
		self.assertEqual(self.kassapaate.maukkaat, 1)

	def test_kateisto_toimii_edullisesti_ei_riittava_maksu(self):
		palautettava = self.kassapaate.syo_maukkaasti_kateisella(300)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		self.assertEqual(palautettava, 300)
		self.assertEqual(self.kassapaate.maukkaat, 0)




	def test_korttiosto_toimii_edullisesti_riittava_maksu(self):
                palautettava = self.kassapaate.syo_edullisesti_kortilla(self.rikaskortti)
                self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
                self.assertEqual(self.kassapaate.edulliset, 1)
                self.assertEqual(palautettava, True)

	def test_korttiosto_toimii_edullisesti_ei_riittava_maksu(self):
                palautettava = self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
                self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
                self.assertEqual(palautettava, False)
                self.assertEqual(self.kassapaate.edulliset, 0)

	def test_korttiosto_toimii_maukkaasti_riittava_maksu(self):
                palautettava = self.kassapaate.syo_maukkaasti_kortilla(self.rikaskortti)
                self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
                self.assertEqual(palautettava, True)
                self.assertEqual(self.kassapaate.maukkaat, 1)

	def test_korttiosto_toimii_edullisesti_ei_riittava_maksu(self):
		palautettava = self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
		self.assertEqual(palautettava, False)
		self.assertEqual(self.kassapaate.maukkaat, 0)

	def test_kortille_lataus(self):
		self.kassapaate.lataa_rahaa_kortille(self.rikaskortti, 200)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

	def test_kortille_lataus_negatiivinen_summa(self):
		self.kassapaate.lataa_rahaa_kortille(self.rikaskortti, -200)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

