# tests/test_calculos.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
"""


import unittest
from core.calculos import evaluar_oportunidad

class TestArbitraje(unittest.TestCase):

  
    def test_oportunidad_positiva(self):
        datos = {
            "ticker": "AAPL",
            "precio_cedear": 14300,   # en ARS
            "precio_nyse": 172,       # en USD
            "ratio": 10,
            "dolar_mep": 895,
        }
        resultado = evaluar_oportunidad(**datos)
        self.assertTrue(resultado['rentabilidad_neta'] > 0)

    def test_sin_oportunidad(self):
        datos = {
            "ticker": "MSFT",
            "precio_cedear": 22500,
            "precio_nyse": 420,
            "ratio": 5,
            "dolar_mep": 895,
        }
        resultado = evaluar_oportunidad(**datos)
        self.assertFalse(resultado['rentabilidad_neta'] > 0)

    def test_igual_dolar_implicito(self):
        datos = {
            "ticker": "GOOGL",
            "precio_cedear": 20000,
            "precio_nyse": 160,
            "ratio": 10,
            "dolar_mep": 1250,
        }
        resultado = evaluar_oportunidad(**datos)
        self.assertAlmostEqual(resultado['rentabilidad_neta'], -0.01, places=2)
if __name__ == '__main__':
    unittest.main()
