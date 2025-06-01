from core.config import COMISION_TOTAL

def evaluar_oportunidad(ticker, precio_cedear, precio_nyse, ratio, dolar_mep):
    dolar_implicito = (precio_cedear * ratio) / precio_nyse
    spread = dolar_mep - dolar_implicito
    rentabilidad_bruta = spread / dolar_implicito
    rentabilidad_neta = rentabilidad_bruta - COMISION_TOTAL

    print(f"\n🔍 Evaluando {ticker}")
    print(f"  Dólar implícito: {dolar_implicito:.2f} ARS/USD")
    print(f"  Spread vs MEP: {spread:.2f} ARS")
    print(f"  Rentabilidad bruta: {rentabilidad_bruta*100:.2f}%")
    print(f"  Rentabilidad neta: {rentabilidad_neta*100:.2f}%")

    if rentabilidad_neta > 0:
        print("✅ Oportunidad detectada!\n")
    else:
        print("❌ No es rentable.\n")

    return {
        "dolar_implicito": dolar_implicito,
        "spread": spread,
        "rentabilidad_bruta": rentabilidad_bruta,
        "rentabilidad_neta": rentabilidad_neta,
    }
