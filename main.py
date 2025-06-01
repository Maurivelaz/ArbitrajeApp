from core.calculos import evaluar_oportunidad

datos = {
    "ticker": "AAPL",
    "precio_cedear": 14300,   # en ARS
    "precio_nyse": 199.95,    # en USD
    "ratio": 10,
    "dolar_mep": 1181.90      # en ARS
}


evaluar_oportunidad(**datos)
