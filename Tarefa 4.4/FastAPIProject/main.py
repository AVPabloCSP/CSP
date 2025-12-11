from fastapi import FastAPI
from conversor import (
    c_to_f, f_to_c, c_to_k,
    metros_a_km, km_a_millas, millas_a_km,
    kg_a_g, g_a_kg, kg_a_lb
)

app = FastAPI(title="API Conversor de Unidades", version="1.0")

@app.get("/")
def inicio():
    return {
        "mensaxe": "Benvido á API de conversión de unidades",
        "endpoints_dispoñibles": [
            "/c_to_f", "/f_to_c", "/c_to_k",
            "/metros_a_km", "/km_a_millas", "/millas_a_km",
            "/kg_a_g", "/g_a_kg", "/kg_a_lb"
        ],
        "probas": "Visita /docs para ver e probar a API"
    }

# --- TEMPERATURAS ---
@app.get("/c_to_f")
def convertir_c_f(c: float):
    return {"Fahrenheit": c_to_f(c)}

@app.get("/f_to_c")
def convertir_f_c(f: float):
    return {"Celsius": f_to_c(f)}

@app.get("/c_to_k")
def convertir_c_k(c: float):
    return {"Kelvin": c_to_k(c)}

# --- DISTANCIAS ---
@app.get("/metros_a_km")
def convertir_m_k(m: float):
    return {"Kilometros": metros_a_km(m)}

@app.get("/km_a_millas")
def convertir_k_m(km: float):
    return {"Millas": km_a_millas(km)}

@app.get("/millas_a_km")
def convertir_mi_km(mi: float):
    return {"Kilometros": millas_a_km(mi)}

# --- PESOS ---
@app.get("/kg_a_g")
def convertir_kg_g(kg: float):
    return {"Gramos": kg_a_g(kg)}

@app.get("/g_a_kg")
def convertir_g_kg(g: float):
    return {"Kilogramos": g_a_kg(g)}

@app.get("/kg_a_lb")
def convertir_kg_lb(kg: float):
    return {"Libras": kg_a_lb(kg)}
