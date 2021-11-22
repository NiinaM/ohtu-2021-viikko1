import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_tilavuudeltaan_negatiivisen_varaston(self):
        varasto1 = Varasto(-1)

        self.assertAlmostEqual(varasto1.tilavuus, 0)

    def test_konstruktori_luo_saldoltaan_negatiivisen_varaston(self):
        varasto2 = Varasto(10,-1)

        self.assertAlmostEqual(varasto2.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_enemmän_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.saldo, 0)    

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_ota_negatiivinen_maara(self):
        paljon_otettiin = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(paljon_otettiin, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)    

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_otetaan_enemman_kuin_varastossa_on_saldoa(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 4)

    def test_tulostaako_src_oikean_tiedon(self):
        self.varasto.lisaa_varastoon(2)
        tuloste = self.varasto.__str__()

        self.assertAlmostEqual(tuloste, "saldo = 2, vielä tilaa 8")    