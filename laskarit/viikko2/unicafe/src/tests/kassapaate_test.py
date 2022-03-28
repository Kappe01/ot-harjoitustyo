import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassan_rahamaaraa_ja_myytyjen_lounaiden_maara(self):
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.maukkaat) , "0")

    def test_edullisen_lounaan_osto_kateisella_onnistuu(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(500)), "260")

    def test_maukkaan_lounaan_osto_kateisella_onnistuu(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(500)), "100")

    def test_edullisen_lounaan_osto_kateisella_ei_onnistu(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(200)), "200")

    def test_maukkaan_lounaan_osto_kateisella_ei_onnistu(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(300)), "300")

    def test_edullisen_lounaan_osto_onnistuu_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(self.kortti.saldo), "760")
        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(self.kortti)), "True")

    def test_maukkaan_lounaan_osto_onnistuu_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(self.kortti.saldo), "600")
        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(self.kortti)), "True")

    def test_edullisen_lounaan_osto_ei_onnistuu_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kortti.saldo), "200")
        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(self.kortti)), "False")

    def test_maukkaan_lounaan_osto_onnistuu_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(self.kortti.saldo), "280")
        self.assertEqual(str(self.kassa.syo_maukkaasti_kortilla(self.kortti)), "False")

    def test_rahan_lataaminen_kortille_onnistuu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(str(self.kortti.saldo), "1200")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100200")

    def test_rahan_lataaminen_kortille_ei_onnistu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(str(self.kortti.saldo), "1000")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
